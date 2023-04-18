from django.shortcuts import render
from django.http import HttpResponse
from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import playercareerstats, playergamelog, leaguegamefinder, scoreboardv2, boxscoresummaryv2, playerprofilev2, teamdetails, teamyearbyyearstats, playerawards, playerdashboardbyyearoveryear, leaguegamefinder,  boxscoretraditionalv2, playernextngames, playoffpicture
from nba_api.stats.library.parameters import SeasonAll
import json
import time
from datetime import date, datetime, timedelta
import numpy as np
import pandas as pd
import itertools
from decimal import *

# Create your views here.
# def home(request):
#     return HttpResponse("Hey Mish")

def active_player_data(request):
    all_players = players.get_players()
    active_players = [player for player in all_players if player["is_active"] == True]

    context = {
        'active_players' : active_players
    }
    return render(request, "all_players.html", context)

def team_data(request):
    all_teams = teams.get_teams()
    context = {
        'all_teams' : all_teams,
    }
    return render(request, "all_teams.html", context)


def box_score_data(request, id):
    game_box_score = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=id)
    player_stats_df = game_box_score.player_stats.get_data_frame().fillna(0)
    # print(player_stats_df.columns)
    team_stats_df = game_box_score.team_stats.get_data_frame().fillna(0)
    starter_bench_stats_df = game_box_score.team_starter_bench_stats.get_data_frame().fillna(0)
    # print(team_stats_df.columns)
    # print(starter_bench_stats_df.columns)

    context = {
        "player_stats" : player_stats_df.to_dict('records'),
        "team_stats" : team_stats_df.to_dict('records'),
        "starter_bench_stats" : starter_bench_stats_df.to_dict('records'),
    }
    return render(request, "box_score.html" , context)

def home(request):
    # games = scoreboardv2.ScoreboardV2(game_date=date.today())
    # games = games.game_header.get_data_frame()
    # games = games.available.get_data_frame()
    games = scoreboardv2.ScoreboardV2(game_date=date.today() - timedelta(days=1))
    #line_Score endpoint
    games_line_score = games.line_score.get_data_frame()
    new_scoreboard_ = games_line_score.groupby(["GAME_SEQUENCE","GAME_ID","TEAM_CITY_NAME"]).agg({'TEAM_CITY_NAME' : ' '.join, 'TEAM_WINS_LOSSES': ' '.join, 'TEAM_ID': 'first', 'PTS':'sum', 'GAME_DATE_EST': ' '.join })
    def uniq(lst):
        for _, grp in itertools.groupby(lst, lambda d: (d['GAME_ID'])):
            yield list(grp)[0]
    box_score_data = games_line_score[["GAME_ID"]]
    box_score_game_ids = list(uniq(box_score_data.to_dict('records')))
    new_list = []
    for bs in box_score_game_ids:
        # print(ns["GAME_ID"])
        box_score = boxscoresummaryv2.BoxScoreSummaryV2(game_id= bs["GAME_ID"])
        game_info_data = box_score.game_info.get_data_frame()
        game_info_data["GAME_ID"] = bs["GAME_ID"]
        merged_df = pd.merge(new_scoreboard_, game_info_data, on="GAME_ID")
        # print(merged_df)
        newest_scoreboard = merged_df.groupby(["GAME_ID","TEAM_CITY_NAME"]).agg({'TEAM_CITY_NAME' : ' '.join, 'TEAM_WINS_LOSSES': ' '.join, 'TEAM_ID': 'first', 'PTS':'sum', 'GAME_DATE_EST': ' '.join, 'ATTENDANCE' : 'sum'})
        new_list.append(newest_scoreboard.to_dict('records'))
    
    context = {
        'scoreboard' : new_list,
    #    'games_today' : games_df.to_dict('records'),
    #    'params' : params.to_dict('records')
    }
    return render(request, "home.html", context)

def conference_standings(request):
     # print(date.today())
    standings = scoreboardv2.ScoreboardV2(game_date=date.today())
    #Conference standings at game_date
    eastern_conference_standings = standings.east_conf_standings_by_day.get_data_frame()
    eastern_conference_standings = eastern_conference_standings[['TEAM', 'G', 'W', 'L', 'W_PCT', 'HOME_RECORD', 'ROAD_RECORD'
            ]]
    western_conference_standings = standings.west_conf_standings_by_day.get_data_frame()
    western_conference_standings = western_conference_standings[['TEAM', 'G', 'W', 'L', 'W_PCT', 'HOME_RECORD', 'ROAD_RECORD'
            ]]
    context = {
        'eastern_conference_standings': eastern_conference_standings.to_dict('records'),
        'western_conference_standings': western_conference_standings.to_dict('records'),
    }
    return render(request, "conference_standings.html", context)
    



def scoreboard_data(request, game_date):
    games = scoreboardv2.ScoreboardV2(game_date=game_date)
    #Conference standings at game_date
    eastern_conference_standings = games.east_conf_standings_by_day.get_data_frame()
    eastern_conference_standings = eastern_conference_standings[['TEAM', 'G', 'W', 'L', 'W_PCT', 'HOME_RECORD', 'ROAD_RECORD'
            ]]
    western_conference_standings = games.west_conf_standings_by_day.get_data_frame()
    western_conference_standings = western_conference_standings[['TEAM', 'G', 'W', 'L', 'W_PCT', 'HOME_RECORD', 'ROAD_RECORD'
            ]]
    team_leaders = games.team_leaders.get_data_frame()
    team_leaders = team_leaders[['TEAM_ABBREVIATION',
            'PTS_PLAYER_NAME', 'PTS',
        'REB_PLAYER_NAME', 'REB', 'AST_PLAYER_NAME', 'AST']]
    series_standings = games.series_standings.get_data_frame()
    context = {
        'eastern_conference_standings': eastern_conference_standings.to_dict('records'),
        'western_conference_standings': western_conference_standings.to_dict('records'),
        'team_leaders': team_leaders.to_dict('records'),
        'series_standings': series_standings.to_dict('records')
    }

    return render(request, "scoreboard.html", context)

def get_one_season_playergamelog(request, id, season):
    game_log_curr_season = playergamelog.PlayerGameLog(player_id=id, season=season)
    game_log_curr_season_df = game_log_curr_season.player_game_log.get_data_frame()
    
    context = {
        "game_log_curr_season_df" : game_log_curr_season_df.to_dict('records')
    }
    return render(request, "player_logs/one_season_playergamelog.html", context )

def get_all_seasons_player_gamelog(request, id):
    game_log_all_seasons = playergamelog.PlayerGameLog(player_id=id, season=SeasonAll.all)
    game_log_all_seasons_df = game_log_all_seasons.player_game_log.get_data_frame()

    context = {
        "game_log_all_seasons" : game_log_all_seasons_df.to_dict('records')
    }
    return render(request, "player_logs/all_seasons_playergamelog.html", context)

def get_pre_season_stats(request, id):
    profile = playerprofilev2.PlayerProfileV2(player_id=id)
    totals_pre_season_df = profile.season_totals_preseason.get_data_frame()

    context = {
        "totals_pre_season" : totals_pre_season_df.to_dict('records'),
    }

    return render(request, "player_logs/pre_season.html", context)

def get_regular_season_stats(request, id):
    profile = playerprofilev2.PlayerProfileV2(player_id=id)
    totals_regular_season_df = profile.season_totals_regular_season.get_data_frame()

    context = {
        "totals_regular_season" : totals_regular_season_df.to_dict('records'),
    }

    return render(request, "player_logs/regular_season.html", context)

def get_post_season_stats(request, id):
    profile = playerprofilev2.PlayerProfileV2(player_id=id)
    totals_post_season_df = profile.season_totals_post_season.get_data_frame()

    context = {
        "totals_post_season" : totals_post_season_df.to_dict('records'),
    }

    return render(request, "player_logs/post_season.html", context)

def get_rankings_regular_season_stats(request, id):
    profile = playerprofilev2.PlayerProfileV2(player_id=id)
    rankings_regular_season_df = profile.season_rankings_regular_season.get_data_frame().fillna(0)

    context = {
        "rankings_regular_season" : rankings_regular_season_df.to_dict('records'),
    }

    return render(request, "player_logs/rankings_regular_season.html", context)

def get_rankings_post_season_stats(request, id):
    profile = playerprofilev2.PlayerProfileV2(player_id=id)
    rankings_post_season_df = profile.season_rankings_post_season.get_data_frame().fillna(0)

    context = {
       "rankings_post_season" : rankings_post_season_df.to_dict('records'),
    }

    return render(request, "player_logs/rankings_post_season.html", context)

def get_player_dashboard(request, id):
    load_stats = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(player_id=id)
    per_year_stats_df = load_stats.by_year_player_dashboard.get_data_frame()
    current_year_stats_df =load_stats.overall_player_dashboard.get_data_frame()
    per_year_stats_df["MIN"] = per_year_stats_df["MIN"].apply(np.ceil)
    current_year_stats_df["MIN"] = current_year_stats_df["MIN"].apply(np.ceil)

    context = {
        "per_year_stats" :  per_year_stats_df.to_dict('records'),
        "current_year_stats" : current_year_stats_df.to_dict('records'),
    }
    return render(request, "player_logs/player_dashboard.html" ,context)


def player_profile(request, id):
    profile = playerprofilev2.PlayerProfileV2(player_id=id)
    next_game_df = profile.next_game.get_data_frame()
    totals_pre_season_df = profile.season_totals_preseason.get_data_frame()
    # career_highs_df = profile.career_highs.get_data_frame()
    # season_highs_df = profile.season_highs.get_data_frame()

    today = datetime.now()
    year = today.year
    player_id = list(totals_pre_season_df["PLAYER_ID"])
    player_id = list(set(player_id))
    all_players = players.get_players()
    player_info = {}
    for player in all_players:
        for p in player_id:
            if player["id"] == p:
                player_info.update(player)
    new_player_info = pd.DataFrame(player_info, index=pd.Series(player_info.pop("is_active")), columns=["id", "full_name", "first_name", "last_name"])
 
    context = {
       "next_game" : next_game_df.to_dict('records'),
       "player_info" : new_player_info.to_dict("records"),
       "year" : year - 1

    #    "career_highs" :  career_highs_df.to_dict('records'),
    #    "season_highs" : season_highs_df.to_dict('records'),

    }
    return render(request, "player_profile.html", context)

def team_profile(request, id):
    team_dets = teamdetails.TeamDetails(team_id=id)
    team_history_df = team_dets.team_history.get_data_frame()
    team_background_df = team_dets.team_background.get_data_frame()
    team_awards_championships_df = team_dets.team_awards_championships.get_data_frame()
    team_awards_conf_df = team_dets.team_awards_conf.get_data_frame()
    team_awards_div_df = team_dets.team_awards_div.get_data_frame()
    team_hof_df = team_dets.team_hof.get_data_frame()
    team_retired_df = team_dets.team_retired.get_data_frame()

    years = teamyearbyyearstats.TeamYearByYearStats(team_id=id)
    years_stats_df = years.team_stats.get_data_frame().fillna(0)
    years_stats_df = years_stats_df.tail(10)

    team_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=id)
    team_games_df = team_games.league_game_finder_results.get_data_frame()
    team_games_df = team_games_df.head(10)

    context = {
        "team_awards_championships" : team_awards_championships_df.to_dict('records'),
        "team_awards_conf" : team_awards_conf_df.to_dict('records'),
        "team_awards_div" : team_awards_div_df.to_dict('records'),
        "team_history" : team_history_df.to_dict('records'),
        "team_background" : team_background_df.to_dict('records'),
        "team_hof" : team_hof_df.to_dict('records'),
        "team_retired" : team_retired_df.to_dict('records'),

        "years_stats" : years_stats_df.to_dict('records'),
        "team_games" : team_games_df.to_dict('records'),
    }

    return render(request, "team_profile.html", context)

def playoffs_data(request):
    playoffs = playoffpicture.PlayoffPicture(league_id="00", season_id=22021)
    east_conf_playoff_picture_df = playoffs.east_conf_playoff_picture.get_data_frame()
    east_conf_standings_df = playoffs.east_conf_standings.get_data_frame()
    east_conf_remaining_games_df = playoffs.east_conf_remaining_games.get_data_frame()
    west_conf_playoff_picture_df = playoffs.west_conf_playoff_picture.get_data_frame()
    west_conf_standings_df = playoffs.west_conf_standings.get_data_frame()
    west_conf_remaining_games_df = playoffs.west_conf_remaining_games.get_data_frame()

    context = {
        "east_conf_playoff_picture" : east_conf_playoff_picture_df.to_dict('records'),
        "east_conf_standings" : east_conf_standings_df.to_dict('records'),
        "east_conf_remaining_games" : east_conf_remaining_games_df.to_dict('records'),
        "west_conf_playoff_picture" : west_conf_playoff_picture_df.to_dict('records'),
        "west_conf_standings" : west_conf_standings_df.to_dict('records'),
        "west_conf_remaining_games" : west_conf_remaining_games_df.to_dict('records'),
    }
    
    return render(request, "playoffs.html", context)

