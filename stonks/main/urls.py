from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search, name="search"),
    path('single_stock', views.get_single_stock, name='single_stock')
]
