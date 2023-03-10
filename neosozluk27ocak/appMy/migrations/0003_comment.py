# Generated by Django 4.1.5 on 2023-02-13 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0002_category_alter_sozluk_date_now_sozluk_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name='Yorumu Yapan')),
                ('title', models.CharField(max_length=50, verbose_name='Yorum Başlığı')),
                ('text', models.TextField(max_length=1000, verbose_name='Yorum')),
                ('date_now', models.DateTimeField(auto_now_add=True, verbose_name='Paylaşım Zamanı')),
                ('sozluk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.sozluk', verbose_name='Sozluk')),
            ],
        ),
    ]
