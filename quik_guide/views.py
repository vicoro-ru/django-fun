from django.shortcuts import render
from .models import Article

# Create your views here.

def main(request):
    return render(request, 'quik_guide/main.html', None)

def news(request):
    a_list = Article.objects.all()
    return render(request, 'quik_guide/news.html', a_list)