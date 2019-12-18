from django.urls import path

from. import views
urlpatterns = [
    path('list', views.list, name = 'list'),
    path('list_c', views.list_c, name = 'list_c'),
    path('Selenium', views.Selenium, name = 'Selenium'),
    path('craw', views.craw, name = 'craw'),
    # path('list_ca', views.list_ca, name = 'list_ca'),
]