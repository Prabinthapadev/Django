from django.shortcuts import render,redirect
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home')
]