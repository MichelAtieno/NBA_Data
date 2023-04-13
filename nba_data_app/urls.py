from django.urls import path
from .views import  home, team_data, active_player_data, scoreboard_data , player_profile, team_profile, box_score_data

# get_one_season_player, get_all_seasons_player, 

app_name="nba_data_app"

urlpatterns = [
    path('', home, name="home"),
    path('all_teams', team_data, name="team_data"),
    path('active_players', active_player_data, name="active_player_data"),
    # path('player/<id>&<season>', get_one_season_player, name="get_one_season_player"),
    # path('player/<id>', get_all_seasons_player, name="get_all_seasons_player"),
    path('player/<id>', player_profile, name="player_profile"),
    path('team/<id>', team_profile, name="team_profile"),
    path('game/<id>', box_score_data, name="box_score_data"),
    path('scoreboard/<game_date>', scoreboard_data, name="scoreboard_data")
]

