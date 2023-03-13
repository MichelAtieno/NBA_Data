from django.urls import path
from .views import  home, team_data, active_player_data, get_one_season_player, get_all_seasons_player  

app_name="nba_data_app"

urlpatterns = [
    path('', home, name="home"),
    path('all_teams', team_data, name="team_data"),
    path('active_players', active_player_data, name="active_player_data"),
    path('player/<id>&<season>', get_one_season_player, name="get_one_season_player"),
    path('player/<id>', get_all_seasons_player, name="get_all_seasons_player")
]

