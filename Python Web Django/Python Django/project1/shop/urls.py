from django.urls import path

from . import views   # 현재 패키지에서 views 모듈을 가져옴

urlpatterns = [
    path('index', views.index, name='index'),
    path('insert', views.insert, name='insert'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),
    path('select', views.select, name='select'),
    path('graph', views.graph, name='graph'),
    path('dataframe', views.dataframe, name='dataframe'),
    path('select1', views.select1, name='select1'),
    path('dataframe_item', views.dataframe_item, name='dataframe_item'),
    path('insert_multi', views.insert_multi, name='insert_multi'),
    path('update_multi', views.update_multi, name='update_multi'),
    path('delete_multi', views.delete_multi, name='delete_multi'),
]
