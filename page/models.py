from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Whoweare(models.Model):
	body = RichTextField(verbose_name='Кто мы')
	img = models.ImageField(upload_to='images/whoweare', verbose_name='Кто мы изображение')
	class Meta:
		verbose_name='Кто мы'


class Whatwedo(models.Model):
	title = models.CharField(max_length=500, verbose_name='Заголовок')
	icon = models.CharField(max_length=300, verbose_name='Класс иконки')
	link = models.CharField(max_length=200, verbose_name='Ссылка')
	body = RichTextField(verbose_name='Что мы делаем')
	class Meta:
		verbose_name='Что мы делаем'
	def __str__(self):
		return self.title

class Fact(models.Model):
	title = models.CharField(max_length=500, verbose_name='Заголовок')
	icon = models.CharField(max_length=300, verbose_name='Класс иконки')
	number = models.CharField(max_length=10,verbose_name='Цифра')
	class Meta:
		verbose_name='Факты'
	def __str__(self):
		return self.title

class Lastwork(models.Model):
	img = models.ImageField(upload_to='images/last', verbose_name='Изображения')
	class Meta:
		verbose_name='Последние работы'


class Expectbest(models.Model):
	skills = RichTextField(verbose_name='Что мы делаем хорошо')
	mission = RichTextField(verbose_name='Наша миссия')
	value = RichTextField(verbose_name='Наша цель')
	class Meta:
		verbose_name='Что мы лучше всего делаем'

class Team(models.Model):
	img = models.ImageField(upload_to='images/team',verbose_name='Аватар')
	name = models.CharField(max_length=300, verbose_name='Имя')
	position = models.CharField(max_length=300, verbose_name='Должность')
	class Meta:
		verbose_name='Команда'

class Review(models.Model):
	name = models.CharField(max_length=300, verbose_name='Имя')
	position = models.CharField(max_length=300, verbose_name='Должность')
	img = models.ImageField(upload_to='images/team', verbose_name='Аватар')
	body = RichTextField(verbose_name='Содержание')
	class Meta:
		verbose_name='Отзывы'
	def __str__(self):
		return self.name

class Banner(models.Model):
	title = models.CharField(max_length=300, verbose_name='Заголовок')
	img = models.ImageField(upload_to='images/banner', verbose_name='Изображение')
	caption = models.CharField(max_length=1000, verbose_name='Захват')
	body = RichTextField(verbose_name='Содержание' ,blank=True)
	link = models.CharField(max_length=200, verbose_name='Ссылка на страницу', blank=True)
	class Meta:
		verbose_name='Баннер'
		verbose_name_plural='Баннеры'
	def __str__(self):
		return self.title
		
		

class Page(models.Model):
	title = models.CharField(max_length=300, verbose_name='Название')
	pre_title = models.CharField(max_length=500, verbose_name='Title в заголовок', blank=True)
	description = models.TextField(verbose_name='Описание')
	img = models.ImageField(upload_to='images/page', verbose_name='Изображение')
	slug = models.SlugField(verbose_name='url')
	banner = models.ManyToManyField(Banner, blank=True, verbose_name='Баннер')
	body = RichTextField(blank=True, verbose_name='Содержание')
	top = models.BooleanField(default=False, verbose_name='Шапка страницы')
	whoweare = models.BooleanField(default=False, verbose_name='Кто мы')
	whatwedo = models.BooleanField(default=False, verbose_name='Что мы делаем')
	fact = models.BooleanField(default=False, verbose_name='Факты')
	lastwork = models.BooleanField(default=False, verbose_name='Последние работы')
	portfolio = models.BooleanField(default=False, verbose_name='Портфолио')
	expectbest = models.BooleanField(default=False, verbose_name='Делаем лучше')
	team = models.BooleanField(default=False, verbose_name='Команда')
	review = models.BooleanField(default=False, verbose_name='Отзывы')
	blog = models.BooleanField(default=False, verbose_name='Блог')
	order = models.BooleanField(default=False, verbose_name='Заказать сайт')
	class Meta:
		verbose_name='Страница'
		verbose_name_plural='Страницы'

	def __str__(self):
		return self.title

class Section(models.Model):
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    body = RichTextField(blank=True, verbose_name='Содержание') 
    page = models.ForeignKey(Page, verbose_name='Страница к которой принадлежит')
    class Meta:
	    verbose_name='Секции'
	    verbose_name_plural='Секция'
    def __str__(self):
	    return self.title

class FeedBack(models.Model):
	name = models.CharField(max_length=200, verbose_name='Имя')
	phone = models.CharField(max_length=12, default='12', verbose_name='Телефон')
	message = models.TextField(verbose_name='Комментарий')
	class Meta:
		verbose_name='Обратная связь'
		verbose_name_plural='Письма от пользователей'
	def __str__(self):
		return self.name
