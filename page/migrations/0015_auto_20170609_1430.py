# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-09 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0014_auto_20170609_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='img',
            field=models.ImageField(upload_to='images/team', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='review',
            name='position',
            field=models.CharField(max_length=300, verbose_name='Должность'),
        ),
    ]
