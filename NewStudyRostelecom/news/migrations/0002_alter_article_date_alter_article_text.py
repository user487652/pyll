# Generated by Django 4.2.8 on 2023-12-25 10:53

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2023, 12, 25, 14, 53, 53, 536594), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(120)], verbose_name='Текст новости'),
        ),
    ]
