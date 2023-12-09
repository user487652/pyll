from django import forms
from django.core.validators import MinLengthValidator

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, FileInput, Select


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           initial='Имя')
    email = forms.EmailField()
    message = forms.CharField(widget=forms.TextInput, disabled=False)
    # demo = forms.BooleanField(required = False, help_text='Текст-подсказка',
    #                           label='Вам нравится?',
    #                           initial=True)
