from django.urls import path
from .views import  home, team_data, active_player_data, scoreboard_data , player_profile, team_profile, box_score_data, get_one_season_playergamelog, get_all_seasons_player_gamelog, get_player_dashboard, playoffs_data

# get_one_season_player, get_all_seasons_player, 

app_name="nba_data_app"

urlpatterns = [
    path('', home, name="home"),
    path('all_teams', team_data, name="team_data"),
    path('active_players', active_player_data, name="active_player_data"),
    path('player/<id>&<season>', get_one_season_playergamelog, name="get_one_season_playergamelog"),
    path('all_seasons/<id>', get_all_seasons_player_gamelog, name="get_all_seasons_playergamelog"),
    path('dashboard/<id>', get_player_dashboard, name="player_dashboard"),
    path('player/<id>', player_profile, name="player_profile"),
    path('tpleam/<id>', team_profile, name="team_profile"),
    path('game/<id>', box_score_data, name="box_score_data"),
    path('scoreboard/<game_date>', scoreboard_data, name="scoreboard_data"),
    path('playoffs', playoffs_data, name="playoff_data"),

]

