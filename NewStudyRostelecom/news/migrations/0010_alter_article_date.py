# Generated by Django 4.2.8 on 2023-12-23 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_article_date_alter_article_text_viewcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2023, 12, 23, 21, 8, 59, 16480), verbose_name='Дата публикации'),
        ),
    ]
