# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-12 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0023_auto_20170612_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.BooleanField(default=False, verbose_name='Заказать сайт'),
        ),
    ]
