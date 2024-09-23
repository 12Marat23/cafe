from django.contrib import admin
from .models import *


# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    """
    Админ-класс для управления сообщениями от пользователей.

    Атрибуты:
        prepopulated_fields (dict): Поля, которые автоматически заполняются на основе других полей (например, slug на основе name).
        list_display (tuple): Поля, которые отображаются в списке объектов в админке.
        list_filter (tuple): Поля, по которым можно фильтровать объекты в админке.
        search_fields (tuple): Поля, по которым можно производить поиск объектов в админке.
        save_as (bool): Позволяет сохранять объекты как новые. По умолчанию - False.
        save_on_top (bool): Отображает кнопку "Сохранить" в верхней части формы. По умолчанию - False.
    """
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'email', 'phone', 'short_description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email',)
    save_as = True  # 'Сохранить как', сохраняет как новый объект. По умолчанию - False.
    save_on_top = True  # 'Сохранить' наверху


class CoffeesAdmin(admin.ModelAdmin):
    """
    Админ-класс для управления статьями о кофе.

    Атрибуты:
        prepopulated_fields (dict): Поля, которые автоматически заполняются на основе других полей (например, slug на основе title).
        list_display (tuple): Поля, которые отображаются в списке объектов в админке.
        list_filter (tuple): Поля, по которым можно фильтровать объекты в админке.
        search_fields (tuple): Поля, по которым можно производить поиск объектов в админке.
        save_as (bool): Позволяет сохранять объекты как новые. По умолчанию - False.
        save_on_top (bool): Отображает кнопку "Сохранить" в верхней части формы. По умолчанию - False.
    """
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'short_description', 'image', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    save_as = True  # 'Сохранить как', сохраняет как новый объект. По умолчанию - False.
    save_on_top = True  # 'Сохранить' наверху


class CommentAdmin(admin.ModelAdmin):
    """Админ-класс для управления комментариями пользователей.
        Атрибуты:
        prepopulated_fields (dict): Поля, которые автоматически заполняются на основе других полей (например, slug на основе title).
        list_display (tuple): Поля, которые отображаются в списке объектов в админке.
        list_filter (tuple): Поля, по которым можно фильтровать объекты в админке.
        search_fields (tuple): Поля, по которым можно производить поиск объектов в админке.
        save_as (bool): Позволяет сохранять объекты как новые. По умолчанию - False.
        save_on_top (bool): Отображает кнопку "Сохранить" в верхней части формы. По умолчанию - False.
    """
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'short_description', 'image', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    save_as = True  # 'Сохранить как', сохраняет как новый объект. По умолчанию - False.
    save_on_top = True  # 'Сохранить' наверху`


admin.site.register(Coffees, CoffeesAdmin)
admin.site.register(ContactMessage, MessageAdmin)
admin.site.register(Comment, CommentAdmin)
