from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    value = 10
    n1 = News('Новость1', 'Текст1', '07.11.2023')
    n2 = News('Новость2', 'Текст2', '22.11.2023')
    l = [n1,n2]
    context = {'title': 'Страница главная', 'Header1': 'Заголовок1', 'value': value, 'numbers': l}
    return render(request, 'main/index.html', context=context)


#
def SideBar(request):
    return render(request, 'main/SideBar.html')
#
# def contact(request):
#     return render(request, 'main/contact.html')
# # Create your views here.
