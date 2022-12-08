from django.contrib import admin
from django.urls import path
from django.urls import path,include 
from .views import *

urlpatterns = [
    path('index',index,name='index'),
    path('',home,name='home'),
    # path('adminlanding',showme,name='showme'),
    # path('adminlanding',adminlanding2,name='adminlanding2'),
    path('adminlogin',adminlogin,name='adminlogin'),
    path('about',about,name='about'),
    path('gallery',gallery,name='gallery'),
    path('dashboard',dashboard,name='dashboard'),
    path('adminlanding',adminlanding,name='adminlanding'),
    path('submitted',submitted,name='submitted'),
    path('del_item/<int:myid>/',del_item, name='del_item')
]