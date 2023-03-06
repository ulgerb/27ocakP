from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

class Profil(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    name = models.CharField(("Profil Adı"), max_length=50)
    image = models.ImageField(("Profil Resmi"), upload_to="profil", max_length=100)
    
    def __str__(self):
        return self.user.username
    
class UserInfo(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    password = models.CharField(("Password"), max_length=50)
    phone_number = PhoneField(blank=True, help_text='Telefon Numarası')

    
