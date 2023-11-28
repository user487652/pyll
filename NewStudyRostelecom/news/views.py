from django.shortcuts import render
from .models import *


# Create your views here.

def news_list(request):
    # news = Article.objects.filter(author=request.user.id)
    news = Article.objects.all()
    context = {'news': news}
    return render(request, 'news/news_list.html', context)


def news_detail(request,id):
    news = Article.objects.get(id=id)
    context = {'news': news}
    return render(request, 'news/news_detail.html', context)
