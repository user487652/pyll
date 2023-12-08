from django.db import models
from django.contrib.auth.models import User
import datetime

class Tag(models.Model):
    title = models.CharField(max_length=80)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', 'status']
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

class Article(models.Model):
    categories = (('E', 'Economics'),
                  ('S', 'Science'),
                  ('IT', 'IT'))
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField('Название', max_length=50, default='')
    anouncement = models.TextField('Аннотация', max_length=250)
    text = models.TextField('Текст новости')
    date = models.DateTimeField('Дата публикации', auto_created=True,default=datetime.datetime.now())
    category = models.CharField(choices=categories, max_length=20, verbose_name='Категории')
    tags=models.ManyToManyField(to=Tag, blank=True)

    def __str__(self):
        return f'Новость: {self.title} от {self.date}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    # def tag_list(self):
    #     s=''
    #     for t in self.tags.all():
    #         s+=t.title+' '
    #     return s



    class Meta:
        ordering=['title','date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

