# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-11 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0015_auto_20170609_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatwedo',
            name='link',
            field=models.CharField(default='sd', max_length=200, verbose_name='Ссылка'),
        ),
    ]
