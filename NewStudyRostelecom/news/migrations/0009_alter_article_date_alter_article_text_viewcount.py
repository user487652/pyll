# Generated by Django 4.2.8 on 2023-12-21 19:21

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2023, 12, 21, 23, 21, 26, 780550), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(200)], verbose_name='Текст новости'),
        ),
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('view_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='news.article')),
            ],
            options={
                'ordering': ('-view_date',),
                'indexes': [models.Index(fields=['-view_date'], name='news_viewco_view_da_c81d57_idx')],
            },
        ),
    ]
