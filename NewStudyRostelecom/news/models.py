from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.safestring import mark_safe
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    title = models.CharField(max_length=80)
    status = models.BooleanField(default=True)

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
    text = models.TextField('Текст новости', validators=[MinLengthValidator(120)])
    date = models.DateTimeField('Дата публикации', auto_created=True, default=datetime.datetime.now())
    category = models.CharField(choices=categories, max_length=20, verbose_name='Категории')
    tags = models.ManyToManyField(to=Tag, blank=True)

    def __str__(self):
        return f'Новость: {self.title} от {self.date}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def image_tag(self):
        image = Image.objects.filter(article=self)
        if image:
            return mark_safe(f'<img src="{image[0].image.url}" height="50px" width="auto"/>')
        else:
            return '(no image)'

    def get_views(self):
        return self.views.count()

    # def tag_list(self):
    #     s=''
    #     for t in self.tags.all():
    #         s+=t.title+' '
    #     return s

    class Meta:
        ordering = ['title', 'date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='article_images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50px" width="auto"/>')
        else:
            return '(no image)'

class ViewCount(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,
                                related_name='views')
    ip_address = models.GenericIPAddressField()
    view_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-view_date',)
        indexes = [models.Index(fields=['-view_date'])]

    def __str__(self):
        return self.article.title


