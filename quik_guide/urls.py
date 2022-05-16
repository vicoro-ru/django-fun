from django import views
from django.urls import re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.main, name='quik-guide'),
    re_path(r'^news/$', views.news, name='news'),
    re_path(r'^articles/', include([
        re_path(r'^$', views.article, name='article'),
        re_path(r'^(?P<year>[\d]{4})/', include([
            re_path(r'^$', views.year, name='year'),
            re_path(r'^(?P<mount>[\d]{1,2})/', include([
                re_path(r'^$', views.mount, name='mount'),
                re_path(r'^(?P<id>[\d]+)/$', views.id, name='article_detail'),
            ]))
        ])),
    ])),
]
