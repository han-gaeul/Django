from unicodedata import name
from django import views
from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    # 영화 데이터 목록 조회
    path('', views.movies, name='movies'),

    # 영화 데이터 정보 조회
    path('<int:pk>/', views.detail, name='detail'),

    # 영화 데이터 생성
    path('create/', views.create, name='create'),

    # 영화 데이터 수정
    path('<int:pk>/update/', views.update, name='update'),

    # 영화 데이터 삭제
    path('<int:pk>/delete/', views.delete, name='delete'),
]
