from django.contrib import admin
from .models import *


# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'email', 'phone', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email',)
    save_as = True  # 'Сохранить как', сохраняет как новый объект. По умолчанию - False.
    save_on_top = True  # 'Сохранить' наверху


class CoffeesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'short_description', 'image', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    save_as = True  # 'Сохранить как', сохраняет как новый объект. По умолчанию - False.
    save_on_top = True  # 'Сохранить' наверху


admin.site.register(Coffees, CoffeesAdmin)
admin.site.register(ContactMessage, MessageAdmin)
