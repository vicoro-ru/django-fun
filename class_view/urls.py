from django.urls import re_path, include
from django.views.generic import  TemplateView
from . import views

app_name='class_view'

urlpatterns = [
    re_path(r'^', include([
        re_path(r'^$', views.index, name='index'),
        re_path(r'^template-views/$', TemplateView.as_view(template_name='class_view/template.html'), name='template_views'),
        re_path(r'^about/$', views.AboutTemplateVies.as_view(), name='about'),
        re_path(r'^head/$', views.HeadTemplateList.as_view(), name='head'),
    ]))
]
