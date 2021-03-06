# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-09 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0013_auto_20170609_1403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name': 'Портфолио', 'verbose_name_plural': 'Портфолио'},
        ),
        migrations.AddField(
            model_name='review',
            name='img',
            field=models.ImageField(default=1, upload_to='images/team', verbose_name='Аватар'),
        ),
        migrations.AddField(
            model_name='review',
            name='position',
            field=models.CharField(default=1, max_length=300, verbose_name='Должность'),
        ),
    ]
