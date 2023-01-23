# Generated by Django 4.1.5 on 2023-01-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название: ')),
                ('description', models.TextField(verbose_name='Описание: ')),
                ('image', models.ImageField(upload_to='product_images', verbose_name='Изображение')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
        ),
    ]
