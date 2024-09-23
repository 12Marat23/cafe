from django.db import models
from django.urls import reverse


# Create your models here.
class Coffees(models.Model):
    """
    Модель для представления статьи о кофе.

    Атрибуты:
        title (CharField): Название статьи.
        slug (SlugField): Уникальная ссылка для статьи, используемая в URL.
        content (TextField): Основной текст статьи.
        image (ImageField): Изображение, связанное с статьей.
        created_at (DateTimeField): Дата и время создания статьи.

    Метаданные:
        verbose_name (str): Человекочитаемое название модели в единственном числе.
        verbose_name_plural (str): Человекочитаемое название модели во множественном числе.
        ordering (list): Порядок сортировки статей по дате создания.
    """

    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='Ссылка')
    content = models.TextField(verbose_name='Статья')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        """Возвращает строковое представление статьи (название)."""
        return self.title

    def short_description(self):
        """
        Возвращает короткое описание статьи, состоящее из первых 100 символов.
        Returns:
            str: Короткое описание статьи с добавлением многоточия в конце.
        """
        return self.content[:100]+'...'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['created_at']

    def get_absolute_url(self):
        """
        Возвращает абсолютный URL для доступа к данной статье.
        Returns:
            str: URL статьи, сформированный на основе slug.
        """
        return reverse('coffee', kwargs={'slug': self.slug})


class ContactMessage(models.Model):
    """
    Модель для представления сообщения от пользователя.

    Атрибуты:
        name (CharField): Имя отправителя сообщения.
        slug (SlugField): Уникальная ссылка для сообщения, используемая в URL.
        email (EmailField): Email адрес отправителя.
        phone (CharField): Телефонный номер отправителя (необязательный).
        message (TextField): Текст сообщения.
        created_at (DateTimeField): Дата и время создания сообщения.

    Метаданные:
        verbose_name (str): Человекочитаемое название модели в единственном числе.
        verbose_name_plural (str): Человекочитаемое название модели во множественном числе.
        ordering (list): Порядок сортировки сообщений по дате создания (от новых к старым).
    """
    name = models.CharField(max_length=100, verbose_name='Имя')
    slug = models.SlugField(max_length=100, verbose_name='Ссылка')
    email = models.EmailField(max_length=100, verbose_name='Email')
    phone = models.CharField(max_length=100, verbose_name='Телефон', blank=True)
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        """Возвращает строковое представление сообщения (имя отправителя)."""
        return self.name

    def short_description(self):
        """
        Возвращает короткое описание сообщения, состоящее из первых 100 символов.
        Returns:
            str: Короткое описание сообщения с добавлением многоточия в конце.
        """
        return self.message[:100] + '...'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']


class Comment(models.Model):
    """
     Модель для представления сообщения от пользователя.
    """
    name = models.CharField(max_length=100, verbose_name='Имя')
    slug = models.SlugField(max_length=100, verbose_name='Ссылка')
    comment = models.TextField(verbose_name='Комментарий')
    image = models.ImageField(upload_to='comments/%Y/%m/%d', verbose_name='Фото', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    def short_description(self):
        """
        Возвращает короткое описание сообщения, состоящее из первых 100 символов.
        Returns:
            str: Короткое описание сообщения с добавлением многоточия в конце.
        """
        return self.comment[:100] + '...'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']