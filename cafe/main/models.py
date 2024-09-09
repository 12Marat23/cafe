from django.db import models
from django.urls import reverse


# Create your models here.
class Coffees(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='Ссылка')
    content = models.TextField(verbose_name='Статья')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('coffee', kwargs={'slug': self.slug})


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    slug = models.SlugField(max_length=100, verbose_name='Ссылка')
    email = models.EmailField(max_length=100, verbose_name='Email')
    phone = models.CharField(max_length=100, verbose_name='Телефон', blank=True)
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']