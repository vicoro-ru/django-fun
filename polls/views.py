#from django.shortcuts import render
from re import template
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.

def index(request):
    q_list = Question.objects.order_by('-pub_date')[:5]
    content = {'q_list': q_list}
    i_template = loader.get_template('polls/index.html')
    return HttpResponse(i_template.render(content, request))


def detail(request, question_id):
#    try:
#        question = Question.objects.get(id=question_id)
#    except Question.DoesNotExist:
#        raise Http404('Заданный опрос не найден')
#    content = {'content': question}
#    return render(request, 'polls/detail.html', content)
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def result(request, question_id):
    message_text = 'Вы просматриваете результаты опроса %s'
    return HttpResponse(message_text % question_id)

def vote(request, question_id):
    return HttpResponse('Вы голосуете в вопросе %s.' % question_id)