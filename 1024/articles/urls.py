from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk/>', views.detail, name='detial'),
    path('create/', views.create, name='create'),
]