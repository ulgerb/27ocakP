from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','user', 'category', 'price', 'stars')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','slug')
    
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','slug')
    
@admin.register(SizeNumber)
class SizeNumberAdmin(admin.ModelAdmin):
    list_display = ('product','id', 'color', 'size', 'stok')


@admin.register(SizeLetter)
class SizeLetterAdmin(admin.ModelAdmin):
    list_display = ('product','id', 'color', 'stok_s',
                    'stok_m', 'stok_l', 'stok_xl')


@admin.register(ProductStok)
class ProductStokAdmin(admin.ModelAdmin):
    list_display = ('product','id')



