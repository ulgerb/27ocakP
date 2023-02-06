from django.db import models

# SQL Tablosu oluşturmak için modelleme yapılır
# python manage.py makemigrations (Tablo oluşturma)
# python manage.py migrate (App Güncelleme)

class Card(models.Model):
    title = models.CharField(max_length=50, verbose_name="Başlık")
    text = models.TextField(("Kart Özellikleri"),max_length=500 )
    category = models.CharField(("Kategori"),max_length=50)
    active = models.BooleanField(("Göster"),null=True)
    brand = models.CharField(("Marka"), max_length=50,null=True,blank=True)
    # null= True , içeriği boş kalabilmesine izin verir ve null değeri gönderir
    def __str__(self): # admin panelinde objeleri isimlendirir
        return self.title
    

class Product(models.Model):
    title = models.CharField( max_length=50)
    price = models.IntegerField()
    stars = models.FloatField()
    
    def __str__(self):  # admin panelinde objeleri isimlendirir
        return self.title
