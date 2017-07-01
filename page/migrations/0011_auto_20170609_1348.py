# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-09 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_auto_20170609_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastwork',
            name='body',
        ),
        migrations.AlterField(
            model_name='lastwork',
            name='img',
            field=models.ImageField(upload_to='images', verbose_name='Изображения'),
        ),
        migrations.RemoveField(
            model_name='page',
            name='lastwork',
        ),
        migrations.AddField(
            model_name='page',
            name='lastwork',
            field=models.ManyToManyField(to='page.Lastwork', verbose_name='Последние работы'),
        ),
    ]