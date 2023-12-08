
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.news_detail, name='news_detail'),
    path('', views.news_list, name='news_list'),
    # path('load', views.news_load, name='news_load'),

]
