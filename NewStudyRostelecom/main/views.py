from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    if request.method == 'POST':
        print('получили пост запрос')
        print(request.POST)
    else:
        print('получили гет запрос')
        print(request.path)
    value = 10
    # n1 = News('Новость1', 'Текст1', '07.11.2023')
    # n2 = News('Новость2', 'Текст2', '22.11.2023')
    # l = [n1, n2]
    water = Product('Добрый мин-ка', 40, 2)
    chocolate = Product('Бабаевский', 40, 12)
    colors = ['red', 'blue', 'golden', 'black']
    context = {'colors': colors,
               'water': water,
               'chocolate': chocolate}

    # context = {'title': 'Страница главная', 'Header1': 'Заголовок1', 'value': value, 'numbers': l}
    return render(request, 'main/MainPage.html', context=context)


def about(request):
    if request.method == 'POST':
        print('получили пост запрос')
        print(request.POST)
    else:
        print('получили гет запрос')
        print(request.path)

    return render(request, 'main/About.html')

def contacts(request):
    if request.method == 'POST':
        print('получили пост запрос')
        print(request.POST)
    else:
        print('получили гет запрос')
        print(request.path)

    return render(request, 'main/Contacts.html')

def registration(request):
    if request.method == 'POST':
        print('получили пост запрос')
        print(request.POST)
    else:
        print('получили гет запрос')
        print(request.path)

    return render(request, 'main/Registration.html')

def account(request):
    if request.method == 'POST':
        print('получили пост запрос')
        print(request.POST)
    else:
        print('получили гет запрос')
        print(request.path)

    return render(request, 'main/Account.html')

def allnews(request):
    if request.method == 'POST':
        print('получили пост запрос')
        print(request.POST)
    else:
        print('получили гет запрос')
        print(request.path)

    newslist_ = []
    newslist = [
        'В Южной Америке проведена успешная акция по защите исчезающих видов грызунов, благодаря которой удалось спасти популяцию редкого вида капибары.', \
        'Ученые из Южной Америки обнаружили новый вид грызуна, который ранее не был известен науке. Это открытие поможет лучше понять биоразнообразие региона и разработать меры по его сохранению.', \
        'В природных заповедниках Южной Америки проведена программа по восстановлению популяции дикарей, что привело к увеличению численности этих животных в их естественной среде обитания.', \
        'В Южной Америке стартовал проект по созданию новых заповедников для защиты уникальных видов грызунов, которые находятся под угрозой исчезновения из-за разрушения их среды обитания.', \
        'Местные организации провели кампанию по борьбе с незаконной торговлей мехами грызунов в Южной Америке, что помогло привлечь внимание к проблеме и защитить этих животных от браконьеров.']
    anounces = ['Успешная акция в Южной Америке спасла редкий вид капибары от исчезновения', \
                'Ученые из Южной Америки обнаружили новый вид грызуна', \
                'Восстановление популяций диких животных в природных заповедниках Южной Америки',
                'Начался проект по созданию новых заповедников в Южной Америке',
                'Кампания по борьбе с незаконной торговлей мехами грызунов в Южной Америке привлекла внимание к проблеме'
                ]

    cntr = 1
    for i in range(0, len(newslist)):
        lst_ = ['Новость ' + str(cntr), newslist[i], anounces[i], '0' + str(cntr) + '.11.2023', 'News/'+str(i)]
        newslist_.append(lst_)
        cntr += 1

    context = {'newslist': newslist_}

    # context = {'title': 'Страница главная', 'Header1': 'Заголовок1', 'value': value, 'numbers': l}
    return render(request, 'main/AllNews.html', context=context)

def News(request, a):
    newslist_ = []
    newslist = [
        'В Южной Америке проведена успешная акция по защите исчезающих видов грызунов, благодаря которой удалось спасти популяцию редкого вида капибары.', \
        'Ученые из Южной Америки обнаружили новый вид грызуна, который ранее не был известен науке. Это открытие поможет лучше понять биоразнообразие региона и разработать меры по его сохранению.', \
        'В природных заповедниках Южной Америки проведена программа по восстановлению популяции дикарей, что привело к увеличению численности этих животных в их естественной среде обитания.', \
        'В Южной Америке стартовал проект по созданию новых заповедников для защиты уникальных видов грызунов, которые находятся под угрозой исчезновения из-за разрушения их среды обитания.', \
        'Местные организации провели кампанию по борьбе с незаконной торговлей мехами грызунов в Южной Америке, что помогло привлечь внимание к проблеме и защитить этих животных от браконьеров.']
    anounces = ['Успешная акция в Южной Америке спасла редкий вид капибары от исчезновения', \
                'Ученые из Южной Америки обнаружили новый вид грызуна', \
                'Восстановление популяций диких животных в природных заповедниках Южной Америки',
                'Начался проект по созданию новых заповедников в Южной Америке',
                'Кампания по борьбе с незаконной торговлей мехами грызунов в Южной Америке привлекла внимание к проблеме'
                ]
    cntr = 1
    for i in range(0, len(newslist)):
        lst_ = ['Новость ' + str(cntr), newslist[i], anounces[i], '0' + str(cntr) + '.11.2023', 'News/'+str(i)]
        newslist_.append(lst_)
        cntr += 1

    context = {'news': newslist_[a]}
    return render(request, 'main/News.html', context=context)

def get_demo(request, a, b):
    return HttpResponse(f'Вы ввели: {a} и {b} \n Сумма:{a + b}')


def custom_404(request, exception):
    return HttpResponse(f'абырвалг:{exception}')

#
# def SideBar(request):
#     return render(request, 'main/sidebar.html')
#
# def contact(request):
#     return render(request, 'main/contact.html')
# # Create your views here.
