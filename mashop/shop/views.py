from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .utils import DataMixin


# Create your views here.

def index(request):
    return render(request, 'index.html')


class AerienHome(DataMixin, TemplateView):
    template_name = 'index.html'
    title_page = 'Aerien shop'
    menu_active = 0

class AerienAbout(DataMixin, TemplateView):
    template_name = 'index.html'
    title_page = 'Aerien shop'
    menu_active = 1

class AerienCatalog(DataMixin, TemplateView):
    template_name = 'index.html'
    title_page = 'Aerien shop'
    menu_active = 2

class AerienReviews(DataMixin, TemplateView):
    template_name = 'index.html'
    title_page = 'Aerien shop'
    menu_active = 3

class AerienContacts(DataMixin, TemplateView):
    template_name = 'index.html'
    title_page = 'Aerien shop'
    menu_active = 4

