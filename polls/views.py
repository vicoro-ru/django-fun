from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Question, Choise


# Create your views here.

# def index(request):
#     '''
#     Page views list of questions
#     '''
#     q_list = Question.objects.order_by('-pub_date')[:5]
#     content = {'q_list': q_list}
#     i_template = loader.get_template('polls/index.html')
#     return HttpResponse(i_template.render(content, request))


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'q_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


def detail(request, pk):
    try:
        question = Question.objects.get(id=pk)
    except Question.DoesNotExist:
        raise Http404('Заданный опрос не найден')
        content = {'content': question}
        return render(request, 'polls/detail.html', content)
    question = get_object_or_404(Question, id=pk)
    return render(request, 'polls/detail.html', {'question': question})


def result(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/result.html', {'question': question})

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        choise = question.choise_set.get(pk=request.POST['choice'])
    except (KeyError, Choise.DoesNotExist):
        error_message = 'Необходимо выбрать один из вариантов'
        return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)), {'questionw': question, 'error_message': error_message})
    else:
        choise.votes += 1
        choise.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
