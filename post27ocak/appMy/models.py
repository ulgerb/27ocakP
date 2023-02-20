from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    
    def __str__(self):
        return self.title
class Post(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("İçerik"), max_length=500)
    date_now = models.DateField(("Tarih"), auto_now_add=True)
    post_url = models.URLField(("Url Adresi"), max_length=200)
    image1 = models.FileField(("Fotoğraf 1"), upload_to="", max_length=100)    
    image2 = models.FileField(("Fotoğraf 2"), upload_to="", max_length=100, null=True, blank=True)
    image3 = models.FileField(("Fotoğraf 3"), upload_to="", max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
