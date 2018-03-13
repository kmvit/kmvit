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


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=12, blank=True)
    city = models.ForeignKey(City)
    email = models.EmailField(blank=True)
    company = models.CharField(max_length=200, blank=True)
    site = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Deal(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    born = models.DateField(verbose_name='Дата', default=datetime.now)
    contact = models.ForeignKey(Contact, verbose_name='Имя')
    stage = models.ForeignKey(Stage, verbose_name='Этап')
    prepayment = models.IntegerField(verbose_name='Предоплата', blank=True, null=True)
    budget = models.IntegerField(verbose_name='Бюджет')
    description = models.TextField(verbose_name='Примечания', blank=True)


    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
        ordering = ['-born']
    def __str__(self):
        return self.title

    def remainder(self):
        try:
            return self.budget - self.prepayment
        except:
            return self.budget
    remainder.short_description = 'Остаток'
