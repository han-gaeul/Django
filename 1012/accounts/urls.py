from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 회원 가입 페이지
    # http://127.0.0.1:8000/accounts/signup/
    path('signup/', views.signup, name='signup'),
    # 회원 조회 페이지 (프로필)
    # http://127.0.0.1:8000/accounts/<user_pk>/
    path('detail/<int:pk>', views.detail, name='detail'),
    # 로그인
    path('login/', views.login, name='login'),
    # 로그아웃
    path('logout/', views.logout, name='logout'),
]
