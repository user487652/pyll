from django.shortcuts import render, HttpResponse
from .models import *
import pandas as pd
import random

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

def news_load(request):
    cntr=Article.objects.count()+1
    df=pd.read_excel(r'C:/Users/Pavel/Downloads/news_gpt.xlsx', dtype='string')
    id_list=User.objects.all().values('id')
    lst=[]
    for lst_ in id_list:
        lst.append(lst_.get('id'))
    for r in range(0,df.shape[0]):
        id_=random.randint(0,len(lst)-1)
        author=User.objects.get(id=lst[id_])
        title='Новость ' + str(cntr)
        anouncement=df.loc[r, 'anounce']
        text=df.loc[r, 'text']
        new_article=Article(author=author,title=title,anouncement=anouncement,text=text)
        new_article.save()
        cntr+=1
    return HttpResponse('Новости добавлены')

