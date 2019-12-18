from django.urls import path

from. import views
urlpatterns = [
    path('join', views.join, name = 'join'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('delete', views.delete, name = 'delete'),
    path('edit', views.edit, name = 'edit'),    
]