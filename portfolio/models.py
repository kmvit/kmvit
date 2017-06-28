from django.db import models

# Create your models here.

class Portfolio(models.Model):
	title = models.CharField(max_length=300, verbose_name='Название')
	img = models.ImageField(upload_to='images/portfolio',verbose_name='Изображение')
	position = models.CharField(max_length=200, verbose_name='Позиция', default='social')
	thumb = models.ImageField(upload_to='images/portfolio/thumb', verbose_name='Превью')
	width = models.CharField(max_length=30, blank=True, verbose_name='Ширина')
	height = models.CharField(max_length=30,blank=True, verbose_name='Высота')
	link = models.URLField(verbose_name='Ссылка')
	class Meta:
		verbose_name='Портфолио'
		verbose_name_plural = 'Портфолио'

	def __str__(self):
		return self.title