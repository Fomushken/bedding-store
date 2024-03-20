from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from cart.forms import CartAddProductForm
from .utils import DataMixin
from .models import Product, ProductsReviews
from .forms import ReviewCreateForm


class AerienHome(DataMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'products'
    title_page = 'Catalog - Aerien shop'
    menu_active = 0
    cat_selected = 0

    def get_queryset(self):
        return Product.objects.filter(is_published=True).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_add_form = CartAddProductForm()
        return self.get_mixin_context(context,
                                      cart_add_form=cart_add_form)


class AerienCategory(DataMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_published=True).filter(category__slug=self.kwargs['category_slug']).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['products'][0].category
        cart_add_form = CartAddProductForm()
        return self.get_mixin_context(context,
                                      title=f'Catalog - {category.name}',
                                      cat_selected=category.pk,
                                      cart_add_form=cart_add_form)


class ShowProduct(DataMixin, DetailView):
    template_name = 'product.html'
    model = Product
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        cart_add_form = CartAddProductForm()
        return self.get_mixin_context(context, title=context['product'].name,
                                      cart_add_form=cart_add_form)
    
    def get_object(self, queryset: QuerySet[Any] | None = None) -> Model:
        return get_object_or_404(Product.objects.filter(is_published=True), slug=self.kwargs[self.slug_url_kwarg])


class AerienReviews(DataMixin, TemplateView):
    template_name = 'reviews.html'
    title_page = 'Reviews - Aerien shop'
    menu_active = 2


class AerienContacts(DataMixin, TemplateView):
    template_name = 'contacts.html'
    title_page = 'Contacts - Aerien shop'
    menu_active = 3


class ProductReview(DataMixin, ListView):
    model = ProductsReviews
    template_name = 'product_reviews.html'
    context_object_name = 'reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(slug=self.kwargs['product_slug'])
        title = 'Reviews for {}'.format(product.name)
        return self.get_mixin_context(context,product = product, title=title)

    def get_queryset(self):
        return ProductsReviews.objects.filter(product_id=Product.objects.get(slug=self.kwargs['product_slug']).id)

    def get_object(self, queryset=None):
        return get_object_or_404(Product.objects.filter(is_published=True), slug=self.kwargs['product_slug'])

class ProductsReviewCreate(DataMixin, CreateView):
    form_class = ReviewCreateForm
    template_name = 'create_review.html'
    title_page = 'Review'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        w = form.save(commit=False)
        w.author = self.request.user
        w.product = Product.objects.get(slug=self.kwargs['product_slug'])
        return super().form_valid(form)