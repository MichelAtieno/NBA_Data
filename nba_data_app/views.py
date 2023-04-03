from django.shortcuts import render
from django.http import HttpResponse
from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import playercareerstats, leaguegamelog, playergamelog, leaguegamefinder
from nba_api.stats.library.parameters import SeasonAll
import json

# Create your views here.
# def home(request):
#     return HttpResponse("Hey Mish")

def home(request):
    all_teams = teams.get_teams()
    context = {
       'all_teams' : json.dumps(all_teams)
    }
    return render(request, "home.html", context)

def active_player_data(request):
    all_players = players.get_players()
    active_players = [player for player in all_players if player["is_active"] == True]
    context = {
        'active_players' :  json.dumps(active_players)
    }
    return render(request, "active_players.html", context)

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

def team_data(request):
    all_teams = teams.get_teams()
    context = {
        'all_teams' : all_teams,
    }
    return render(request, "all_teams.html", context)
