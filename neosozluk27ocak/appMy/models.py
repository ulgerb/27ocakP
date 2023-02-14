from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    
    def __str__(self):
        return self.title

class Sozluk(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE,null=True)
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("İçerik Yazısı"),max_length=2000)
    date_now = models.DateTimeField(("Tarih"), auto_now_add=True)
    image = models.FileField(("Fotoğraf"), upload_to='', max_length=100)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    sozluk = models.ForeignKey(Sozluk, verbose_name=("Sozluk"), on_delete=models.CASCADE)
    user = models.CharField(("Yorumu Yapan"), max_length=50)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    text = models.TextField(("Yorum"), max_length=1000)
    date_now = models.DateTimeField(("Paylaşım Zamanı"), auto_now_add=True)
    
    def __str__(self):
        return self.sozluk.title
