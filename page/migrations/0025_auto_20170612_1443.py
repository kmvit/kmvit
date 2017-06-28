# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-12 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0024_page_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='fact',
        ),
        migrations.AddField(
            model_name='page',
            name='fact',
            field=models.BooleanField(default=False, verbose_name='Факты'),
        ),
        migrations.RemoveField(
            model_name='page',
            name='lastwork',
        ),
        migrations.AddField(
            model_name='page',
            name='lastwork',
            field=models.BooleanField(default=False, verbose_name='Последние работы'),
        ),
        migrations.RemoveField(
            model_name='page',
            name='whatwedo',
        ),
        migrations.AddField(
            model_name='page',
            name='whatwedo',
            field=models.BooleanField(default=False, verbose_name='Что мы делаем'),
        ),
    ]
