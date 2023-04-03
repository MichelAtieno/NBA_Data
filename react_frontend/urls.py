from django.urls import path
from .views import  index

app_name="react_frontend"

urlpatterns = [
    path('', index, name="index"),
]