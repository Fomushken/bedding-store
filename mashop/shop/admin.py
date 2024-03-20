from django.contrib import admin

from .models import Category, Product, ProductsGallery, ProductsReviews


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = ProductsGallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated', 'is_published']
    inlines = [GalleryInline, ]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available', 'is_published']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ProductsReviews)
class ProductReviewsAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'rating']
