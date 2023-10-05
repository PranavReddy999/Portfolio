from django.contrib import admin
from django.urls import path,include
from base import views

urlpatterns = [
    
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects')
]
