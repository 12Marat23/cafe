from django.db import models
from django.urls import reverse


# Create your models here.
class Shop(models.Model):
    """
    Модель Shop представляет товар в интернет-магазине.
    """
    product = models.CharField(max_length=100, verbose_name='Наименование товара')  # Наименование товара
    slug = models.CharField(max_length=100, verbose_name='Ссылка')  # Ссылка на товар
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Фото', blank=True)  # Фото товара
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')  # Стоимость товара
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Скидка', blank=True,
                                   null=True)  # Скидка товара

    def __str__(self):
        """
        Возвращает строковое представление объекта Shop.
        """
        return self.product

    def short_description(self):
        """
        Возвращает сокращенное описание товара.
        """
        return self.description[:100] + '...'

    def get_absolute_url(self):
        """
        Возвращает абсолютный URL для товара на основе его 'slug'.
        """
        return reverse('product', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['product']
