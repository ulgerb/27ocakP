# Generated by Django 4.1.5 on 2023-03-13 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productstok',
            name='images',
            field=models.ManyToManyField(to='appMy.productimg', verbose_name='Ürün Fotoğrafları'),
        ),
    ]
