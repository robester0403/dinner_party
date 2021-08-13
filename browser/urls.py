from django.shortcuts import render
from django.urls import path, include

from . import views

urlpatterns = [
    # recipes index /recipes/
    path('', views.index, name='index'),
    path('allitems/', views.allitems),
    path('bycountry/', views.country),
    path('byid/<id>/', views.pksearch), 
    path('bymaintype/<main_type>/', views.foodtype)
]