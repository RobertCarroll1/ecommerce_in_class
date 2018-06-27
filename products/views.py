from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product  

# Create your views here.
def get_products(request): 
    products=Product.objects.all()
    return render(request, 'products/productlist.html',{"products":products})