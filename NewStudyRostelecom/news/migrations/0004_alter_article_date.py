# Generated by Django 4.2.8 on 2024-01-10 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2024, 1, 10, 12, 40, 37, 757663), verbose_name='Дата публикации'),
        ),
    ]
