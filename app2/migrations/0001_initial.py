# Generated by Django 5.2.1 on 2025-05-28 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Заголовок')),
                ('URL_name', models.SlugField(max_length=200, unique=True, verbose_name='Слаг')),
                ('content', models.TextField(verbose_name='Контент')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
        ),
    ]
