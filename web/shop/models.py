from django.db import models
from django.urls import reverse


# Create your models here.

class Web(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Опис товару")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Час створення")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Час редагування")
    is_published = models.BooleanField(default=True, verbose_name="Публікація")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категорії")
    price = models.CharField(max_length=20, verbose_name='Ціна')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Мій сайт з автозапчастинами'
        verbose_name_plural = 'Мій сайт з автозапчастинами'
        ordering = ['-time_update', 'title']


# class UserProfile(models.Model):
#     username = models.CharField(max_length=30, verbose_name="Нік користувача")
#     first_name = models.CharField(max_length=30, verbose_name="Ім'я користувача")
#     last_name = models.CharField(max_length=30, verbose_name="Фамілія користувача")
#     photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото користувача")
#     status = models.CharField(max_length=20, verbose_name="Статус користувача")
#     slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL користувача")
#
#     def __str__(self):
#         return self.username
#
#     class Meta:
#         verbose_name = 'Інформація про користувачів'
#         verbose_name_plural = 'Інформація про користувачів'
#         ordering = ['username', 'first_name']

class Pay(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Опис товару")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    price = models.CharField(max_length=20, default=True, verbose_name='Ціна')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pay', kwargs={'pay_slug': self.slug})

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплата товару'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категорії товару'
        verbose_name_plural = 'Категорії товару'
        ordering = ['id', 'name']