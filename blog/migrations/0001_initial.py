# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-12 10:12
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(auto_created=models.CharField(max_length=300, verbose_name='Название'), verbose_name='URL')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('img', models.ImageField(upload_to='images/blog', verbose_name='Изображение')),
                ('born', models.DateField(default=datetime.date(2017, 6, 12), verbose_name='Дата')),
                ('body', ckeditor.fields.RichTextField(verbose_name='Содержание')),
            ],
            options={
                'verbose_name_plural': 'Блог',
                'verbose_name': 'Блог статья',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(auto_created=models.CharField(max_length=300, verbose_name='Название'), verbose_name='URL')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Категории',
                'verbose_name': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(auto_created=models.CharField(max_length=300, verbose_name='Название'), verbose_name='URL')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Тэги',
                'verbose_name': 'Тэг',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Tag', verbose_name='Тэги'),
        ),
    ]