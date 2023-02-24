from django.db import models
from django.contrib.auth.models import User
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

# USER MODEL
class UserInfoStatus(models.Model):
    user=models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    title=models.CharField(("Yetenek Adı"), max_length=50)
    statu=models.IntegerField(("Yetenek Değeri"), default=0)

    def __str__(self):
        return "KULLANICI: "+ self.user.username +"...........YETENEK: "+ self.title
    
class UserInfo(models.Model):
    user=models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    password=models.CharField(("Şifre"), max_length=50)
    job= models.CharField(("İş"), max_length=50,default="-")
    image=models.FileField(("Fotoğraf"), upload_to=None, max_length=100,default='None/download.jpg')
    phone=models.CharField(("Telefon Numarası"), max_length=50, default="-")
    adress=models.CharField(("Adres"), max_length=50, default="-")
    status=models.ManyToManyField(UserInfoStatus, verbose_name=("Yetenekler") )

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    name = models.CharField(("İsim"), max_length=50)
    email = models.EmailField(("Email"), max_length=254)
    title = models.CharField(("Konu"), max_length=50)
    text = models.TextField(("Mesaj"), max_length=500)
    
    def __str__(self):
        return self.name
