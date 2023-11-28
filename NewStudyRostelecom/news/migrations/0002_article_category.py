# Generated by Django 4.2.6 on 2023-11-23 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('E', 'Economics'), ('S', 'Science'), ('IT', 'IT')], default=0, max_length=20),
            preserve_default=False,
        ),
    ]
