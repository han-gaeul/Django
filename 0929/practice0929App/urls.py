from django.urls import path
from . import views

# url namespace
# url을 이름으로 분류하는 기능
app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('editupdate/<int:pk>', views.editupdate, name='editupdate'),
]