from django.contrib import admin
from.models import *


# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product',)}
    list_display = ('id', 'product', 'short_description', 'image', 'price', 'discount')
    list_filter = ('product',)
    search_fields = ('product',)
    save_as = True  # 'Сохранить как', сохраняет как новый объект. По умолчанию - False.
    save_on_top = True  # 'Сохранить' наверху


admin.site.register(Shop, ShopAdmin)