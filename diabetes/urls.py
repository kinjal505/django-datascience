from django.shortcuts import render
from django.urls import path
from diabetes import views
urlpatterns = [
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
   path('prediction/',views.prediction,name='prediction'),
   path('login/',views.home,name='home'),
   path('registration/',views.about,name='about')
]