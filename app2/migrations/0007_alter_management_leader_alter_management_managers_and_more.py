# Generated by Django 5.2.1 on 2025-06-03 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0006_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Руководитель', to='app2.person'),
        ),
        migrations.AlterField(
            model_name='management',
            name='managers',
            field=models.ManyToManyField(related_name='Менеджеры', to='app2.person'),
        ),
        migrations.AlterField(
            model_name='program',
            name='benefits',
            field=models.TextField(verbose_name='Преимущества'),
        ),
        migrations.AlterField(
            model_name='program',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='program',
            name='link',
            field=models.URLField(verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
    ]
