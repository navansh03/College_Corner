from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product

class product_list(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'productlist.html'
    context_object_name = 'products'
    paginate_by = 10
