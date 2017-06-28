from django.db import models
from ckeditor.fields import RichTextField
from datetime import date
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    slug = models.SlugField(unique= True, verbose_name='URL')
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='URL')
    class Meta:
        verbose_name='Тэг'
        verbose_name_plural='Тэги'

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='URL')
    img = models.ImageField(upload_to='images/blog', verbose_name='Изображение')
    born = models.DateField(default=timezone.now, verbose_name='Дата')
    category = models.ForeignKey(Category, verbose_name='Категория')
    tags = models.ForeignKey(Tag,verbose_name='Тэги')
    body = RichTextField(verbose_name='Содержание')


    class Meta:
        verbose_name='Блог статья'
        verbose_name_plural = 'Блог'

    def __str__(self):
        return self.title


