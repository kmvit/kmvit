# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-12 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0026_delete_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='top',
            field=models.BooleanField(default=False, verbose_name='Шапка страницы'),
        ),
    ]
