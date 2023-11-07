
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    value=10
    context={'title':'Страница главная','Header1':'Заголовок1','value':value}
    return render(request, 'home/index.html', context=context)
#