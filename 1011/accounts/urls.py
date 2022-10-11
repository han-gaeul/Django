from django.urls import path
from django import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
