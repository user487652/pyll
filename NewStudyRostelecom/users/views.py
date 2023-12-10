from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import Group

def registration(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='Authors')
            user.groups.add(group)
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            authenticate(username=username,password=password)
            messages.success(request, f'{username} был зарегистрирован!')
            return redirect('home')
    else:
        form=UserCreationForm()
    context={'form':form}
    return render(request, 'users/registration.html', context)


def index(request):
    print(request.GET)
    # print(request.user,request.user.id)
    # user_acc=Account.objects.get(user=request.user)
    # print(user_acc.birthday,user_acc.gender )
    return HttpResponse('Приложение Users')

def profile(request):
    return render(request, 'users/profile.html')


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
