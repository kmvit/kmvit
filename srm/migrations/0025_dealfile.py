# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-24 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0024_auto_20180313_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='deal_file')),
                ('deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srm.Deal')),
            ],
        ),
    ]
