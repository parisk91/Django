from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Manufacturer, Product

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"

# Create your views here.
