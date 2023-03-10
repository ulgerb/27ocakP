# Generated by Django 4.1.5 on 2023-02-01 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Ürün Adı')),
                ('price', models.IntegerField(verbose_name='Ürün Fiyatı')),
                ('stars', models.FloatField(verbose_name='Ürün Popülerliği')),
            ],
        ),
        migrations.AlterField(
            model_name='card',
            name='category',
            field=models.CharField(max_length=50, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='card',
            name='text',
            field=models.TextField(max_length=500, verbose_name='Kart Özellikleri'),
        ),
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Başlık'),
        ),
    ]
