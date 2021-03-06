# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-09 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_auto_20170609_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatwedo',
            name='icon',
            field=models.CharField(default=1, max_length=300, verbose_name='Класс иконки'),
        ),
        migrations.AddField(
            model_name='whatwedo',
            name='title',
            field=models.CharField(default=1, max_length=500, verbose_name='Заголовок'),
        ),
        migrations.RemoveField(
            model_name='page',
            name='whatwedo',
        ),
        migrations.AddField(
            model_name='page',
            name='whatwedo',
            field=models.ManyToManyField(to='page.Whatwedo', verbose_name='Что мы делаем'),
        ),
    ]
