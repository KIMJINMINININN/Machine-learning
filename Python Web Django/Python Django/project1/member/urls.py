from django.urls import path

from . import views   # 현재 패키지에서 views 모듈을 가져옴

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('join', views.join, name='join'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
    path('list', views.list, name='list'),
    path('logout', views.logout, name='logout'),
    path('edit', views.edit, name='edit')
]
