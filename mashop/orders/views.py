from django.shortcuts import render
from django.views import View

from cart.cart import Cart
from shop.utils import DataMixin
from .forms import OrderCreateForm
from .models import OrderItem
from .tasks import order_created


class CreateOrderView(DataMixin, View):

    template_name = 'orders/order_create.html'

    def get(self, request):
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
    