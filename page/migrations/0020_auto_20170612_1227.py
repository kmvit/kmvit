# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-12 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0019_portfolio_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='thumb',
            field=models.ImageField(upload_to='images/portfolio/thumb', verbose_name='Превью'),
        ),
    ]
