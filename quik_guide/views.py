from django.shortcuts import render
from .models import Article

# Create your views here.

def main(request):
    a_list = Article.objects.order_by('-pub_date')
    return render(request, 'quik_guide/main.html', {'articles': a_list})

def news(request):
    pass