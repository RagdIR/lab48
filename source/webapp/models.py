from django.db import models

DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = [
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', 'Продукты питания'),
    ('household', 'Хозтовары'),
    ('toys', 'Игрушки'),
    ('electronics', 'Электротовары')
]

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название товара')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=20, verbose_name='Категория', choices=CATEGORY_CHOICES,
                                default=DEFAULT_CATEGORY)
    amount = models.IntegerField(verbose_name='Остаток')
    price = models.DecimalField(verbose_name='Цена', max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.amount} - {self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
