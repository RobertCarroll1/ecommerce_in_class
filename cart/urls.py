from django.urls import path
from .views import *

urlpatterns = [
    path('', get_cart, name="cart"),
    path('add/', add_to_cart, name="add_to_cart"),
    path('remove/', remove_from_cart, name="remove_from_cart"),
]