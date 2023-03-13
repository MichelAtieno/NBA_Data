from django.shortcuts import render
from django.http import HttpResponse
from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import playercareerstats, leaguegamelog, playergamelog, leaguegamefinder
from nba_api.stats.library.parameters import SeasonAll

# Create your views here.
# def home(request):
#     return HttpResponse("Hey Mish")

def home(request):
   
    context = {
       
    }
    return render(request, "home.html", context)

def active_player_data(request):
    all_players = players.get_players()
    # print(all_players
    active_players = [player for player in all_players if player["is_active"] == True]
    context = {
        'active_players' :  active_players 
    }
    return render(request, "active_players.html", context)
    

def team_data(request):
    all_teams = teams.get_teams()
    context = {
        'all_teams' : all_teams,
    }
    return render(request, "all_teams.html", context)
