from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.template import loader
from django.urls import reverse
from polls.models import Question
import requests

# Create your views here.

def index(request):
    return HttpResponse('Hello im index page')

class AboutTemplateVies(TemplateView):
    template_name = 'class_view/about.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse(render(request, 'class_view/get.html'))

    def post(self, request, *args, **kwargs):
        return HttpResponse(loader.get_template('class_view/post.html').render())

class HeadTemplateList(ListView):
    template_name = 'class_view/head.html'
    model = Question


    def get(self, request, *args, **kwargs):
        question = Question.objects.all()
        head = requests.head('http://127.0.0.1:8000/class-view/head/')
        return render(request, 'class_view/head.html', {'question_list': question, 'head': head})

    def head(self, request):
        
        return HttpResponse('Hi ima head response')