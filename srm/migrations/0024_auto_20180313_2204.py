# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-13 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0023_auto_20180313_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='kindofwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srm.KindofWork'),
        ),
    ]