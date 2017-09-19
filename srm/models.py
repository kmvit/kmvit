from django.db import models
from django.db.models import Sum
from datetime import datetime

# Create your models here.

class Stage(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    label = models.CharField(max_length=300, verbose_name='Цвет', default='label-default')
    class Meta:
        verbose_name = 'Этап'
        verbose_name_plural = 'Этапы'
    def __str__(self):
        return self.title
        
class City(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
    def __str__(self):
        return self.title

class Deal(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    born = models.DateField(verbose_name='Дата')
    name = models.CharField(max_length=300, verbose_name='Имя')
    phone = models.CharField(max_length=13, verbose_name='Телефон')
    company = models.CharField(max_length=300, verbose_name='Компания')
    city = models.ForeignKey(City, default=1, verbose_name='Город')
    site = models.CharField(max_length=250, blank=True, verbose_name='Сайт')
    stage = models.ForeignKey(Stage, verbose_name='Этап')
    prepayment = models.IntegerField(verbose_name='Предоплата', blank=True, null=True)
    prepayment_date = models.DateField(verbose_name='Дата предоплаты', null=True, blank=True)
    budget = models.IntegerField(verbose_name='Бюджет')
    
    
    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
    def __str__(self):
        return self.title
        
    def remainder(self):
        try:
            return self.budget - self.prepayment
        except:
            return self.budget
    remainder.short_description = 'Остаток'