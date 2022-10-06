from django import views
from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.movies, name='movies'),
]