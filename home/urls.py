from django.contrib import admin
from django.urls import path
from home import views
from registration import views as regi

urlpatterns = [
   path('',views.index, name='index'),
   path('/',views.index, name='index'),
   path("index",views.index, name='index'),
   path("about",views.about, name='about'),
   path("sarvesh",views.sarvesh, name='sarvesh'),
   path("full_stack",views.full_stack, name='full_stack'),
   path("front_end",views.front_end, name='front_end'),
   path("contact",views.contact, name='contact'),
   path("security",views.security, name='security'),
   path("data_scientist",views.data_scientist,name='data_scientist'),
   path("register",regi.register,name='SignUp'),
   path('login',regi.login, name='login'),
   path('logout',regi.logout, name='logout'),
]
