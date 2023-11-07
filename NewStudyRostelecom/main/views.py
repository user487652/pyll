from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    value=10
    context={'title':'Страница главная','Header1':'Заголовок1','value':value}
    return render(request, 'main/index.html', context=context)
#
def SideBar(request):
    return render(request, 'main/SideBar.html')
#
# def contact(request):
#     return render(request, 'main/contact.html')
# # Create your views here.
