# Generated by Django 4.2.6 on 2023-11-30 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_tag_article_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tag',
            new_name='tags',
        ),
    ]
