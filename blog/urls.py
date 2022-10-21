from django.contrib import admin
from django.urls import path
from blog.views import *
urlpatterns = [
    path('',homepage,name='index'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('category',category,name='category'),
    path('search',search,name='search'),
    path('single',single,name='single'),

    
]
