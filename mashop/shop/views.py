from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .utils import DataMixin
from .models import Product


# Create your views here.

def index(request):
    return render(request, 'index.html')


class AerienHome(DataMixin, TemplateView):
    template_name = 'index.html'
    title_page = 'Aerien shop'
    menu_active = 0


class AerienCatalog(DataMixin, ListView):
    template_name = 'catalog.html'
    context_object_name = 'products'
    title_page = 'Catalog - Aerien shop'
    menu_active = 1

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.filter(is_published=True).select_related('category')


class AerienReviews(DataMixin, TemplateView):
    template_name = 'reviews.html'
    title_page = 'Reviews - Aerien shop'
    menu_active = 2


class AerienContacts(DataMixin, TemplateView):
    template_name = 'contacts.html'
    title_page = 'Contacts - Aerien shop'
    menu_active = 3
