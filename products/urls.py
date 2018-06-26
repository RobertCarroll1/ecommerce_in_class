from django.urls import path
from .views import *

urlpatterns = [
    path('', get_products, name="product_list"),
    path('<int:id>/add/', add_to_cart, name="add_to_cart"),
    
]