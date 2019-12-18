from django.urls import path

from. import views
urlpatterns = [
    path('submit', views.submit, name = 'submit'),
    path('submit_ch', views.submit_ch, name = 'submit_ch'),
    path('submit_ed', views.submit_ed, name = 'submit_ed'),
    path('submit_de', views.submit_de, name = 'submit_de'),
]