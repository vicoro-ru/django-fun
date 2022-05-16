from django import views
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.main, name='quik-guide'),
    re_path(r'^news/$', views.news, name='news'),
]
