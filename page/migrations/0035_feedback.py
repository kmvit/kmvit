# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0034_banner_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Письмо')),
            ],
            options={
                'verbose_name_plural': 'Письма от пользователей',
                'verbose_name': 'Обратная связь',
            },
        ),
    ]
