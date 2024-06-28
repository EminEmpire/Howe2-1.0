from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('trainingcourses/', views.trainingcourses, name='trainingcourses'),
    path('consultancy/', views.consultancy, name='consultancy'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),

]