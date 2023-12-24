from django.shortcuts import render, HttpResponse, redirect
from .models import *
import pandas as pd
import random
import json
from .forms import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Avg, Count, Sum
from django.contrib.auth.models import User
from users.utils import check_group
# Create your views here.

from django.core.paginator import Paginator


def news_list(request):
    categories = Article.categories  # создали перечень категорий
    author_list = User.objects.all()  # создали перечень авторов
    if request.method == "POST":
        selected_author = int(request.POST.get('author_filter'))
        selected_category = int(request.POST.get('category_filter'))
        request.session['selected_author'] = selected_author
        request.session['selected_category'] = selected_category
        if selected_author == 0:  # выбраны все авторы
            news = Article.objects.all().order_by('date')
        else:
            news = Article.objects.filter(author=selected_author)
        if selected_category != 0:  # фильтруем найденные по авторам результаты по категориям
            news = news.filter(category__icontains=categories[selected_category - 1][0])
    else:  # если страница открывется
        selected_author = request.session.get('selected_author')
        print(selected_author)
        if selected_author != None and selected_author != 0:  # если не пустое - находим нужные новости
            news = Article.objects.filter(author=selected_author)
        else:
            news = Article.objects.all().order_by('date')
        selected_category = request.session.get('selected_category')
        print(selected_category)
        if selected_category != None and selected_category != 0:  # если не пустое - находим нужные ноновсти
            news = news.filter(category__icontains=categories[selected_category - 1][0])
    print(news)
    total = len(news)
    p = Paginator(news, 5)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {'news': page_obj, 'author_list': author_list, 'selected_author': selected_author,
               'categories': categories, 'selected_category': selected_category, 'total': total}

    return render(request, 'news/news_list.html', context)


def news_detail(request, id):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwraded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    ip_address = ip
    news = Article.objects.get(id=id)
    images = Image.objects.filter(article_id=id)
    ViewCount.objects.get_or_create(article=news, ip_address=ip_address)
    context = {'news': news, 'images': images}
    return render(request, 'news/news_detail.html', context)


def news_load(request):
    cntr = Article.objects.count() + 1
    df = pd.read_excel(r'C:/Users/Pavel/Downloads/news_gpt.xlsx', dtype='string')
    id_list = User.objects.all().values('id')
    lst = []
    for lst_ in id_list:
        lst.append(lst_.get('id'))
    for r in range(0, df.shape[0]):
        id_ = random.randint(0, len(lst) - 1)
        author = User.objects.get(id=lst[id_])
        title = 'Новость ' + str(cntr)
        anouncement = df.loc[r, 'anounce']
        text = df.loc[r, 'text']
        new_article = Article(author=author, title=title, anouncement=anouncement, text=text)
        new_article.save()
        cntr += 1
    return HttpResponse('Новости добавлены')


@check_group('Authors')
@login_required(login_url=settings.LOGIN_URL)
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            if current_user.id != None:
                new_article = Article()
                new_article.author = current_user
                new_article.title = form.cleaned_data.get('title')
                new_article.anouncement = form.cleaned_data.get('anouncement')
                new_article.text = form.cleaned_data.get('text')
                new_article.save()
                new_article.tags.set(form.cleaned_data.get('tags'))
                for img in request.FILES.getlist('image_field'):
                    Image.objects.create(article=new_article, image=img, title=img.name)
                return redirect('news_list')
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'news/create_article.html', context)


def news_search(request):
    news = {}
    if request.method == 'POST':
        print(request.POST)
        news = Article.objects.filter(title=request.POST.get('search_input')).order_by('date')
    context = {'news': news}
    return render(request, 'news/news_search.html', context)


def search_auto(request):
    news = {}
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        q = request.GET.get('term', '')
        news = Article.objects.filter(title__icontains=q)
        results = []
        for n in news:
            results.append(n.title)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
