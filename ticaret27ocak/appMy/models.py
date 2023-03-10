from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    slug = models.SlugField(("Slug Kategori"), blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title
        
class Color(models.Model):
    title = models.CharField(("Renkler"), max_length=50)
    slug = models.SlugField(("Slug Kategori"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Color, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
        
class Product(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    # color = models.ManyToManyField(Color, verbose_name=("Renkler"))
    image = models.ImageField(("Resim"), upload_to="product", null=True)
    title = models.CharField(("Başlık"), max_length=50)
    brand = models.CharField(("Marka"), max_length=50)
    text = models.TextField(("Açıklama"), max_length=1000)
    detail = models.TextField(("Özellikler"), max_length=800)
    price = models.FloatField(("Fiyat"))
    stars = models.FloatField(("Puan"), default=0)
    
    def __str__(self):
        return self.title
    
class SizeNumber(models.Model):
    # AYAKKABI BEDEN
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    color = models.ForeignKey(Color, verbose_name=("Renk"), on_delete=models.CASCADE)
    # price eklenicek, size foreign olucak, image classı olucak, cinsiyet class
    size = models.IntegerField(("Beden Numarası"))
    stok = models.IntegerField(("Stok sayısı"))
    
    def __str__(self):
        return self.product.title
    
class SizeLetter(models.Model):
    # KIYAFET BEDEN
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    color = models.ForeignKey(Color, verbose_name=("Renk"), on_delete=models.CASCADE)
    stok_s = models.IntegerField(("Small Stok"), default=0)
    stok_m = models.IntegerField(("Medium Stok"), default=0)
    stok_l = models.IntegerField(("Large Stok"), default=0)
    stok_xl = models.IntegerField(("Xlarge Stok"), default=0)

    def __str__(self):
        return self.product.title
    
class ProductStok(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    sizenumber = models.ManyToManyField(SizeNumber, verbose_name=("Ayyakkabı beden ve stok"),blank=True)
    sizeletter = models.ManyToManyField(SizeLetter, verbose_name=("Kıyafet beden ve stok"), blank=True)
    
    def __str__(self):
        return self.product.title
    
    
    
    
    
    
    

