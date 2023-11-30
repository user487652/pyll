from django.shortcuts import render
from .models import *


# Create your views here.

def news_list(request):
    # news = Article.objects.filter(author=request.user.id)
    # news = Article.objects.get(title='Новость 1')
    # print(news)
    # news = Article.objects.filter(author=request.user.id)
    news = Article.objects.all()
    tag=Tag.objects.filter(title='Crypto')[0]
    tagged_news=Article.objects.filter(tags=tag)
    print(tagged_news)
    # tag=Tag.objects.filter(title='IT').first()

    context = {'news': news}
    return render(request, 'news/news_list.html', context)


def news_detail(request,id):
    news = Article.objects.get(id=id)
    context = {'news': news}
    return render(request, 'news/news_detail.html', context)
