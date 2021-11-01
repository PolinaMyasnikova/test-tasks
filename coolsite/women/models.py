from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slag = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Картинка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обнавления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    vil = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Деревня')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'cat_slug': self.slag})

    class Meta:
        verbose_name = 'Персонажи'
        verbose_name_plural = 'Персонажи Наруто'
        ordering = ['title']


class Category(models.Model):
    village = models.CharField(max_length=100, db_index=True, verbose_name='Деревня')
    slag = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.village

    def get_absolute_url(self):
        return reverse('village', kwargs={'vil_id': self.pk})

    class Meta:
        verbose_name = 'Деревня'
        verbose_name_plural = 'Деревни'
        ordering = ['village']
