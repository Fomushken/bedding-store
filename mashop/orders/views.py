from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.utils import DataMixin
from .tasks import order_created
from django.views.generic import CreateView, TemplateView


class CreateOrderView(DataMixin, View):

    template_name = 'orders/order_create.html'

    def get(self, request):
        cart = Cart(request)
        form = OrderCreateForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        cart = Cart(request)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            order_created.delay(order.id)
            return render(request, 'orders/order_created.html', {'order': order})
        return render(request, self.template_name, {'form': form})