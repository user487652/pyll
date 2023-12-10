from django.shortcuts import render, HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm

def registration(request):
    form=UserCreationForm()
    context={'form':form}
    return render(request, 'users/registration.html', context)


def index(request):
    print(request.GET)
    # print(request.user,request.user.id)
    # user_acc=Account.objects.get(user=request.user)
    # print(user_acc.birthday,user_acc.gender )
    return HttpResponse('Приложение Users')


def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print('Сообщение отправлено', form.cleaned_data)
        else:
            print(form.errors)
    else:
        form = ContactForm()
        form.name = 'Любимый клиент'

    context = {'form': form}
    return render(request, 'users/contact_page.html', context)
