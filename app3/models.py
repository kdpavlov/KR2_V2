from django.db import models

class Category(models.Model):
    name = models.CharField('Категория', max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    name = models.CharField('Название товара', max_length=200)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    photo = models.ImageField('Фото', upload_to='products/')
    available = models.BooleanField('В наличии', default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    customer_name = models.CharField('Имя покупателя', max_length=100)
    customer_email = models.EmailField('Email')
    quantity = models.PositiveIntegerField('Количество', default=1)
    created_at = models.DateTimeField('Дата заказа', auto_now_add=True)

    def __str__(self):
        return f"Заказ {self.product.name} от {self.customer_name}"

