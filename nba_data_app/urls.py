from django.urls import path
from .views import home, team_data, active_player_data

app_name="nba_data_app"

urlpatterns = [
    path('', home, name="home"),
    path('all_teams', team_data, name="team_data"),
    path('active_players', active_player_data, name="active_player_data")
]

