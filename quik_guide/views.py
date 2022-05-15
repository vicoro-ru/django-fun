from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.

def main(request):
    a_list = Article.objects.order_by('-pub_date')
    return render(request, 'quik_guide/main.html', {'articles': a_list})

def news(request):
    return HttpResponse('This news page')

def article(request):
    return HttpResponse('This article page')

def year(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'a_list': a_list}
    return render(request, 'quik_guide/year_archive.html', context)

def mount(requst, year, mount):
    return HttpResponse(f'This {year} {mount} article page')

def id(requst, year, mount, id):
    return HttpResponse(f'This article {id} publishec {mount}:{year}')