from django.shortcuts import render
from django.views.generic import ListView
from .models import *


# Create your views here.
def shop(request):
    return render(request, 'shop/shop.html')


class ProductListView(ListView):
    model = Shop
    template_name = 'shop/shop.html'
