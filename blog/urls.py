from django.urls import path
from django.contrib import admin
from blog.views import home_blog, single_blog, test

urlpatterns = [
    path('', home_blog, name='home_blog'),
    path('Single/<int:pid>', single_blog, name='single_blog'),
]
