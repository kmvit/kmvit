# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-12 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0014_deal_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(max_length=200)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srm.City')),
            ],
        ),
        migrations.RemoveField(
            model_name='deal',
            name='city',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='company',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='phone',
        ),
    ]
