from django.shortcuts import render
from django.http import HttpResponse
from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import playercareerstats, leaguegamelog, playergamelog, leaguegamefinder, scoreboardv2, boxscoresummaryv2
from nba_api.stats.library.parameters import SeasonAll
import json
import time
from datetime import date, datetime
import pandas as pd
import itertools

# Create your views here.
# def home(request):
#     return HttpResponse("Hey Mish")

def home(request):
    # games = scoreboardv2.ScoreboardV2(game_date=date.today())
    # games = games.game_header.get_data_frame()
    # games = games.available.get_data_frame()
    games = scoreboardv2.ScoreboardV2()
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
    # print(type(new_list))
    # for l in new_list:
    #     for m in l:
    #         print(m["TEAM_CITY_NAME"])
    
    context = {
        'scoreboard' : new_list
    #    'games_today' : games_df.to_dict('records'),
    #    'params' : params.to_dict('records')

    }
    return render(request, "home.html", context)

def active_player_data(request):
    all_players = players.get_players()
    active_players = [player for player in all_players if player["is_active"] == True]
    context = {
        'active_players' : active_players
    }
    return render(request, "active_players.html", context)

def team_data(request):
    all_teams = teams.get_teams()
    context = {
        'all_teams' : all_teams,
    }
    return render(request, "all_teams.html", context)



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

def box_score_data(request):

    context = {

    }
    return render(request, "box_score.html" , context)


def player_profile(request):
    context = {
       
    }
    return render(request, "home.html", context)


def get_one_season_player(request, id, season:str):
    one_season_game_log = playergamelog.PlayerGameLog(player_id=id, season=season)
    one_season_game_log = one_season_game_log.get_data_frames()[0]
    one_season_game_log_list = one_season_game_log.to_dict('records')

    context = {
        "one_season_game_log_list":  one_season_game_log_list,
        "game_log_list": json.dumps(one_season_game_log_list)
    }
        
    return render(request, "player_info_one_season.html", context)

def get_all_seasons_player(request, id):
    all_seasons_game_log = playergamelog.PlayerGameLog(player_id=id, season=SeasonAll.all)
    all_seasons_game_log =  all_seasons_game_log.get_data_frames()[0]
    all_seasons_game_log_list = all_seasons_game_log.to_dict('records')
    # print(all_seasons_game_log_list)

    context = {
        "all_seasons_game_log_list": all_seasons_game_log_list
    }

    return render(request, "player_info_all_seasons.html", context)

