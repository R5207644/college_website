from django.contrib import admin
from django.urls import path
from registration import views as regi
from home import views as hom


urlpatterns = [
   
   path('login',regi.login, name='login'),
   path('index', hom.index),
   path('logout',regi.logout, name='logout'),
   
]
