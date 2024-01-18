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
