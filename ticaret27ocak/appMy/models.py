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
    slug = models.SlugField(("Slug Renk"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Color, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Gander(models.Model):
    title = models.CharField(("Cinsiyet"), max_length=50)

    def __str__(self):
        return self.title
    
class Size(models.Model):
    title = models.CharField(("Beden"), max_length=50)
    slug = models.SlugField(("Slug Beden"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Size, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Size2(models.Model):
    # s m l xl xxl
    title = models.CharField(("Beden"), max_length=50)
    slug = models.SlugField(("Slug Beden"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Size2, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
class Product(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    # color = models.ManyToManyField(Color, verbose_name=("Renkler"))
    image = models.ImageField(("Resim"), upload_to="product", null=True, blank=True)
    title = models.CharField(("Başlık"), max_length=50)
    brand = models.CharField(("Marka"), max_length=50)
    price = models.FloatField(("Ortalama Fiyat"), null=True)
    text = models.TextField(("Açıklama"), max_length=1000)
    detail = models.TextField(("Özellikler"), max_length=800)
    stars = models.FloatField(("Puan"), default=0)
    
    def __str__(self):
        return self.title

class ProductImg(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    image = models.ImageField(("Resim"), upload_to="product")
    
    def __str__(self):
        return self.product.title
    
class SizeNumber(models.Model):
    # AYAKKABI BEDEN
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    color = models.ForeignKey(Color, verbose_name=("Renk"), on_delete=models.CASCADE)
    size = models.ForeignKey(Size, verbose_name=("Beden Numarası"), on_delete=models.CASCADE, null=True)
    gander = models.ForeignKey(Gander, verbose_name=("Cinsiyet"), on_delete=models.CASCADE, null=True)
    price = models.FloatField(("Fiyat"), default=0)
    stok = models.IntegerField(("Stok sayısı"),default=0)
    
    def __str__(self):
        return self.product.title


class SizeLetter(models.Model):
    # KIYAFET BEDEN
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    color = models.ForeignKey(Color, verbose_name=("Renk"), on_delete=models.CASCADE)
    gander = models.ForeignKey(Gander, verbose_name=("Cinsiyet"), on_delete=models.CASCADE, null=True)
    price = models.FloatField(("Fiyat"),default=0)
    stok = models.IntegerField(("Stok"), default=0)
    size = models.ForeignKey(Size2, verbose_name=("Beden"), on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.product.title
    
class ProductStok(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    images = models.ManyToManyField(ProductImg, verbose_name=("Ürün Fotoğrafları"))
    sizenumber = models.ManyToManyField(SizeNumber, verbose_name=("Ayyakkabı beden ve stok"),blank=True)
    sizeletter = models.ManyToManyField(SizeLetter, verbose_name=("Kıyafet beden ve stok"), blank=True)
    
    def __str__(self):
        return self.product.title
    
    
    
    
    
    
    

