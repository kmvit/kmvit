# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-09 18:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0026_auto_20180324_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('born', models.DateField(default=datetime.datetime.now, verbose_name='Дата')),
                ('content', models.TextField(blank=True, verbose_name='Содержание')),
                ('finish', models.BooleanField(default=False, verbose_name='Завершено')),
                ('deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srm.Deal')),
            ],
            options={
                'verbose_name_plural': 'Задачи',
                'verbose_name': 'Задача',
                'ordering': ['-born'],
            },
        ),
    ]
