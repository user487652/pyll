from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Product

def index(request):
    if  request.method == 'POST':
        print('получили пост запрос')
        print(request.POST)
    else:
        print('получили гет запрос')
    value = 10
    n1 = News('Новость1', 'Текст1', '07.11.2023')
    n2 = News('Новость2', 'Текст2', '22.11.2023')
    l = [n1,n2]
    water = Product('Добрый мин-ка', 40, 2)
    chocolate = Product('Бабаевский', 40, 12)
    colors=['red','blue','golden','black']
    context={'colors':colors,
             'water':water,
             'chocolate':chocolate}

    # context = {'title': 'Страница главная', 'Header1': 'Заголовок1', 'value': value, 'numbers': l}
    return render(request, 'main/index.html', context=context)

def get_demo(request, a, b):
    return HttpResponse(f'Вы ввели: {a} и {b} \n Сумма:{a+b}')

def custom_404(request, exception):
    return HttpResponse(f'абырвалг:{exception}')

#
# def SideBar(request):
#     return render(request, 'main/sidebar.html')
#
# def contact(request):
#     return render(request, 'main/contact.html')
# # Create your views here.
