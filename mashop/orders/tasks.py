from mashop.celery import app
from django.core.mail import send_mail
from .models import Order


@app.task
def order_created(order_id):
    '''
    Task for sending email notification if order succesfully created
    '''
    order = Order.objects.get(id=order_id)
    subject = f'Order number {order_id}'
    message = (f'Dear {order.first_name}, \n\nYou have succesfully placed an order.\n'
               f'Your order is {order.id}')
    mail_sent = send_mail(subject,
                          message,
                          'skinner.fomin@yandex.ru',
                          [order.email])
    return mail_sent
