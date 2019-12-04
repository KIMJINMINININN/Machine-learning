from django.urls import path

from . import views   # 현재 패키지에서 views 모듈을 가져옴

urlpatterns = [
    path('auth_join', views.auth_join, name='auth_join'),
    path('auth_index', views.auth_index, name='auth_index'),
    path('auth_login', views.auth_login, name='auth_login'),
    path('auth_logout', views.auth_logout, name='auth_logout'),
    path('auth_edit', views.auth_edit, name='auth_edit'),
    path('auth_pw', views.auth_pw, name='auth_pw'),
]