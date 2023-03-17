from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','user', 'category', 'stars')


@admin.register(ProductImg)
class ProductImgAdmin(admin.ModelAdmin):
    list_display = ('product', 'id')
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
    list_display = ('product','id', 'color', 'size','stok')


@admin.register(ProductStok)
class ProductStokAdmin(admin.ModelAdmin):
    list_display = ('product','id')

@admin.register(Gander)
class GanderAdmin(admin.ModelAdmin):
    list_display = ('title','id')
    
@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')

@admin.register(Size2)
class Size2Admin(admin.ModelAdmin):
    list_display = ('title', 'id')



@admin.register(Shopbasket)
class ShopbasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_letter',
                    'price_all', 'count', 'id')

    
