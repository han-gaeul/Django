from django.urls import path
from . import views

app_name = 'class1004App'

urlpatterns = [
    path('', views.index, name='index'),
]
