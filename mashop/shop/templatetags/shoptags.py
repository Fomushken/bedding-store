from django import template
from django.db.models import Count

from shop.models import Category

register = template.Library()

@register.inclusion_tag('includes/list_categories.html')
def show_categories(cat_selected=0):
    return {'cats': Category.objects.annotate(total=Count('products')).filter(total__gt=0),
            'cat_selected': cat_selected}

@register.simple_tag
def get_categories():
    return Category.objects.annotate(total=Count('products')).filter(total__gt=0)