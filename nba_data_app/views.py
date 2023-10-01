from django.shortcuts import render
from django.http import HttpResponse
from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import playercareerstats, playergamelog, playergamelogs, leaguegamefinder, scoreboardv2, boxscoresummaryv2, playerprofilev2, teamdetails, teamyearbyyearstats, playerawards, playerdashboardbyyearoveryear, leaguegamefinder,  boxscoretraditionalv2, playernextngames, playoffpicture
from nba_api.stats.library.parameters import SeasonAll
import json
import time
from datetime import date, datetime, timedelta
import numpy as np
import pandas as pd
import itertools
import re
from decimal import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# def home(request):
#     return HttpResponse("Hey Mish")

@api_view(["GET"])
def active_player_data_api(request):
    all_players = players.get_players()
    active_players = [player for player in all_players if player["is_active"] == True]

    return Response(active_players)

@api_view(["GET"])
def player_profile_api(request, id):
    if request.method == "GET":
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

        return Response(context)
    return Response(status.HTTP_404_NOT_FOUND)

def active_player_data(request):
    active_players = players.get_active_players()
   
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

def get_teams_played_by_player():
    active_players = players.get_active_players()
    teams_played = []
    # frequency_count = []
    for player in active_players:
        load_stats = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(player_id=player["id"])
        per_year_stats_df = load_stats.by_year_player_dashboard.get_data_frame()
        per_year_stats_df["MIN"] = per_year_stats_df["MIN"].apply(np.ceil)
        # print(per_year_stats_df.columns)
        per_year_stats_df["PLAYER_ID"] = player["id"]
        per_year_stats_df = per_year_stats_df[["TEAM_ABBREVIATION", "GROUP_VALUE", "PLAYER_ID"]]
        teams_played = per_year_stats_df.to_dict("records")
    teams_played_df = pd.DataFrame(teams_played)
    teams_played_df.to_csv('static/csvs/teams_player_played_in.csv', encoding='utf-8')
    # 
    # team_frequency_count_df = pd.read_csv('static/csvs/teams_player_played_in.csv')

    return

def get_current_team_for_player():
    current_team = []
    active_players = players.get_active_players()
    for player in active_players:
        load_stats = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(player_id= player["id"])
        per_year_stats_df = load_stats.by_year_player_dashboard.get_data_frame()
        per_year_stats_df["MIN"] = per_year_stats_df["MIN"].apply(np.ceil)
        teams_played = per_year_stats_df[["TEAM_ABBREVIATION", "GROUP_VALUE"]]
        teams_played["PLAYER_ID"] = player["id"]
        teams_played = teams_played.iloc[:1]
        current_team.append(teams_played.to_dict("records"))
    current_team_df = pd.DataFrame(current_team)
    current_team_df.to_csv('static/csvs/cuurent_player_team.csv', encoding='utf-8')

    return

def get_active_players_to_csv():
    active_players = players.get_active_players()
    active_players_df = pd.DataFrame(active_players)
    active_players_df.to_csv('active_players.csv', encoding='utf-8')

    return
    

def home(request):
    # games = scoreboardv2.ScoreboardV2(game_date=date.today())
    # games = games.game_header.get_data_frame()
    # games = games.available.get_data_frame()

    ######## BOXSCORE DATA

    # games = scoreboardv2.ScoreboardV2(game_date=date.today() - timedelta(days=1))
    # #line_Score endpoint
    # games_line_score = games.line_score.get_data_frame()
    # new_scoreboard_ = games_line_score.groupby(["GAME_SEQUENCE","GAME_ID","TEAM_CITY_NAME"]).agg({'TEAM_CITY_NAME' : ' '.join, 'TEAM_WINS_LOSSES': ' '.join, 'TEAM_ID': 'first', 'PTS':'sum', 'GAME_DATE_EST': ' '.join })
    # def uniq(lst):
    #     for _, grp in itertools.groupby(lst, lambda d: (d['GAME_ID'])):
    #         yield list(grp)[0]
    # box_score_data = games_line_score[["GAME_ID"]]
    # box_score_game_ids = list(uniq(box_score_data.to_dict('records')))
    # new_list = []
    # for bs in box_score_game_ids:
    #     # print(ns["GAME_ID"])
    #     box_score = boxscoresummaryv2.BoxScoreSummaryV2(game_id= bs["GAME_ID"])
    #     game_info_data = box_score.game_info.get_data_frame()
    #     game_info_data["GAME_ID"] = bs["GAME_ID"]
    #     merged_df = pd.merge(new_scoreboard_, game_info_data, on="GAME_ID")
    #     # print(merged_df)
    #     newest_scoreboard = merged_df.groupby(["GAME_ID","TEAM_CITY_NAME"]).agg({'TEAM_CITY_NAME' : ' '.join, 'TEAM_WINS_LOSSES': ' '.join, 'TEAM_ID': 'first', 'PTS':'sum', 'GAME_DATE_EST': ' '.join, 'ATTENDANCE' : 'sum', 'GAME_ID' : ' '.join})
    #     new_list.append(newest_scoreboard.to_dict('records'))

    ######## SEASONS PLAYER HAS BEEN IN CURRENT TEAM
    
    team_frequency_count_df = pd.read_csv('static/csvs/player_teams.csv')
    frequency_count = team_frequency_count_df.groupby(["TEAM_ABBREVIATION", "PLAYER_ID"]).count()
    frequency_count.reset_index(inplace=True)
    frequency_count.rename(columns = {'Unnamed: 0':'SEASON_COUNT'}, inplace = True)
    frequency_count = frequency_count.sort_values(by=['SEASON_COUNT'], ascending=False)
    frequency_count.reset_index(inplace=True)
    frequency_count = frequency_count.drop(['index', 'GROUP_VALUE'], axis=1)

    curr_team_df = team_frequency_count_df[team_frequency_count_df["GROUP_VALUE"] == "2022-23"]
    curr_team = curr_team_df[["TEAM_ABBREVIATION", "GROUP_VALUE", "PLAYER_ID"]]
    curr_team.reset_index(inplace=True)
    curr_team = curr_team.drop(['index'], axis=1)

    columns_to_compare = ['TEAM_ABBREVIATION', 'PLAYER_ID']
    current_team_df = pd.merge(frequency_count, curr_team , on=columns_to_compare, suffixes=('frequency_count', 'curr_team '), how='outer')
    
    current_team_df["GROUP_VALUE"] = current_team_df["GROUP_VALUE"].replace("2022-23", True)
    current_team_df["GROUP_VALUE"] = current_team_df["GROUP_VALUE"].notna()
    current_team_df.rename(columns = {'GROUP_VALUE':'CURRENT_TEAM'}, inplace = True)

    active_players = pd.read_csv('static/csvs/active_players.csv')

    ######## NO. OF TEAMS PLAYER HAS BEEN IN

    player_teams_df = pd.read_csv('static/csvs/player_teams.csv')
    # player_teams = player_teams_df.groupby("PLAYER_ID")["TEAM_ABBREVIATION"].sum()
    # print(player_teams.column)
    player_teams=( player_teams_df.groupby(["PLAYER_ID", "TEAM_ABBREVIATION"],as_index=False)
           .agg(list)
           .reindex(columns=player_teams_df.columns) ).groupby("PLAYER_ID").count()
    player_teams.rename(columns = {'TEAM_ABBREVIATION':'NO_OF_TEAMS_PLAYED_IN'}, inplace = True)
    player_teams = player_teams.drop(['Unnamed: 0', 'GROUP_VALUE'], axis=1)
    player_teams.reset_index(inplace=True)

    new_df = player_teams_df.groupby("PLAYER_ID").TEAM_ABBREVIATION.agg(['count',','.join])
    # print(player_teams)
    new_df.reset_index(inplace=True)
    new_df = new_df.to_dict("records")
    # new_list = []
    # [new_list.append(nd["join"]) for nd in new_df if nd["join"] not in new_list]
    updated_df = []
    for nd in new_df:
        # print(nd["join"])
        nd["join"] = str(set(nd["join"].split(",")))
        updated_df.append(nd)
    updated_df = pd.DataFrame(updated_df)
    updated_df = updated_df.drop(['count'], axis=1)
    updated_df.rename(columns = {'join':'TEAMS_PLAYED_IN'}, inplace = True)
    cols_to_compare = ['PLAYER_ID']
    teams_played_in = pd.merge(player_teams, updated_df, on=cols_to_compare, suffixes=('player_teams', 'updated_df'), how='outer')
    teams_played_in['TEAMS_PLAYED_IN'] = teams_played_in['TEAMS_PLAYED_IN'].str.replace('{', '').str.replace('}', '').str.replace("'", '')
    
    context = {
        # 'scoreboard' : new_list,
        # "team_frequency_count" :  team_frequency_count.to_dict("records"),
    #    'games_today' : games_df.to_dict('records'),
    #    'params' : params.to_dict('records')
        "current_team" : current_team_df.to_dict("records"),
        "active_players" : active_players.to_dict("records"),
        "player_teams" : teams_played_in.to_dict("records"),
        # "updated_df" :  updated_df.to_dict("records")
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
        "game_log_all_seasons" : game_log_all_seasons_df.to_dict('records'),
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
    # print(per_year_stats_df.columns)
    teams_played = per_year_stats_df[["TEAM_ABBREVIATION", "GROUP_VALUE"]]
    team_frequency_count = teams_played.groupby("TEAM_ABBREVIATION").count()
    team_frequency_count.reset_index(inplace=True)

    context = {
        "per_year_stats" :  per_year_stats_df.to_dict('records'),
        "current_year_stats" : current_year_stats_df.to_dict('records'),
        "teams_played" : teams_played.to_dict('records'),
        "team_frequency_count": team_frequency_count.to_dict('records'),
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

    player_games = leaguegamefinder.LeagueGameFinder(player_id_nullable=id)
    player_games_df = player_games.league_game_finder_results.get_data_frame()
    player_games_df = player_games_df.head(10)
    player_games_df.to_csv('static/csvs/last_10_player_games.csv', encoding='utf-8')
 
    context = {
       "next_game" : next_game_df.to_dict('records'),
       "player_info" : new_player_info.to_dict("records"),
       "year" : year - 1,
       "player_games" : player_games_df.to_dict("records"),
    #    "json_player_games" : json.loads(json_data)

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
    playoffs = playoffpicture.PlayoffPicture(league_id="00", season_id=22022)
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

