from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=60, verbose_name='First Name')
    last_name = models.CharField(max_length=60, verbose_name='Last Name')
    email = models.EmailField(verbose_name='Email')
    delivery = models.BooleanField(default=False, verbose_name='Deliver')
    city = models.CharField(max_length=100, verbose_name='City')
    address = models.CharField(max_length=300, blank=True, verbose_name='Address(if deliver required)')
    postal_code = models.CharField(max_length=20, blank=True, verbose_name='Postal code(if deliver required')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity

