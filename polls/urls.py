from django.urls import re_path, include
from . import views

app_name = 'polls'
urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^(?P<pk>[\d]+)/', include([
        re_path(r'^$', views.detail, name='detail'),
        re_path(r'^result/$', views.result, name='result'),
        re_path(r'^vote/$', views.vote, name='vote')
    ]))
]
