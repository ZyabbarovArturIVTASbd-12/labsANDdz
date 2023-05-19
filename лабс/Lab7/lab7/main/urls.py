from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about),
    path('table_show/<int:tk>', views.table_view, name='table_show'),
    path('table_show/table_id:<int:tk>/row:<int:el>/<command>', views.table_change, name='table_change')
]
