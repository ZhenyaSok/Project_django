from django.db import models
from django.utils import timezone

from config import settings

NULLABLE = {'null':True, 'blank':True}

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(**NULLABLE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'



class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    price = models.FloatField(default=0, verbose_name='Цена за штуку')
    overview = models.TextField(**NULLABLE, verbose_name='Описание')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='пользователь')


    def __str__(self):
        return f'{self.name} ({self.price})'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('price',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Наименование товара')
    num_version = models.IntegerField(verbose_name='номер версии')
    name_version = models.CharField(max_length=100, verbose_name='название версии')
    version_flug = models.BooleanField(verbose_name='признак версии', default=False)

    def __str__(self):
        return f'{self.product} ({self.name_version})'

    """
    Добавьте новую модель «Версия», которая должна содержать следующие поля:
    продукт,
    номер версии,
    название версии,
    признак текущей версии.
    При наличии активной версии реализуйте вывод в список продуктов информации об активной версии."""

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


