# Generated by Django 5.0 on 2024-01-09 14:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория')),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование товара')),
                ('category', models.CharField(max_length=100, verbose_name='Категория')),
                ('photo', models.ImageField(null=True, upload_to='catalog/', verbose_name='Изображение')),
                ('price', models.FloatField(default=0, verbose_name='Цена за штуку')),
                ('overview', models.TextField(null=True, verbose_name='Описание')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'ordering': ('price',),
            },
        ),
    ]
