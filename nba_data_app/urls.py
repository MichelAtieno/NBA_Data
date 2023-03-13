from django.urls import path
from .views import home

app_name="nba_data_app"

urlpatterns = [
    path('', home, name="home"),
]

