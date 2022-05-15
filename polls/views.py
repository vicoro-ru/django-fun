#from django.shortcuts import render
from re import template
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.

def index(request):
    q_list = Question.objects.order_by('-pub_date')[:5]
    content = {'q_list': q_list}
    i_template = loader.get_template('polls/index.html')
    return HttpResponse(i_template.render(content, request))


def detail(request, question_id):
    return HttpResponse('Вы просматриваете опрос %s.' % question_id)

def result(request, question_id):
    message_text = 'Вы просматриваете результаты опроса %s'
    return HttpResponse(message_text % question_id)

def vote(request, question_id):
    return HttpResponse('Вы голосуете в вопросе %s.' % question_id)