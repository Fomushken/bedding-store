from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('show_product', kwargs={'product_slug': self.slug})

    class Meta:
        ordering = ('-created', 'name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class ProductsGallery(models.Model):
    image = models.ImageField(upload_to='images/products/', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

# class ProductsReviews(models.Model):
#     author = models.ForeignKey(get_user_model(), related_name='reviews', on_delete=models)