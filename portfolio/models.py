from django.db import models

# Create your models here.

class Portfolio(models.Model):
	title = models.CharField(max_length=300, verbose_name='Название')
	slug = models.SlugField(default='sdsd')
	img = models.ImageField(upload_to='images/portfolio',verbose_name='Изображение')
	img2 = models.ImageField(upload_to='images/portfolio',verbose_name='Изображение2', blank=True)
	img3 = models.ImageField(upload_to='images/portfolio',verbose_name='Изображение3', blank=True)
	developer = models.CharField(max_length=300, verbose_name="Разработчик", blank=True)
	year = models.IntegerField(verbose_name="Год", default='2017')
	client = models.CharField(max_length=300, verbose_name="Клиент", blank=True)
	skills = models.CharField(max_length=300, verbose_name="Скилы", blank=True)
	description = models.TextField(verbose_name='Описание', blank=True)
	work = models.TextField(verbose_name='Что было сдеано', blank=True)
	position = models.CharField(max_length=200, verbose_name='Позиция', default='social')
	thumb = models.ImageField(upload_to='images/portfolio/thumb', verbose_name='Превью')
	width = models.CharField(max_length=30, blank=True, verbose_name='Ширина')
	height = models.CharField(max_length=30,blank=True, verbose_name='Высота')
	link = models.URLField(verbose_name='Ссылка')
	class Meta:
		verbose_name='Портфолио'
		verbose_name_plural = 'Портфолио'
		ordering=['-id']
	def __str__(self):
		return self.title