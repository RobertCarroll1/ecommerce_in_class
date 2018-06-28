from django.shortcuts import render, get_object_or_404, HttpResponse, redirect 
from products.models import Product

# Create your views here.
def get_cart(request):
    cart = request.session.get('cart', {})
    cart_total = 0
    products = []
    for p in cart:
        product = get_object_or_404(Product, pk=p)
        products.append({
            'product': product,
            'quantity': cart[p],
            'total': product.price * cart[p]
        })

        cart_total += product.price * cart[p]
        
    return render(request, "cart/cart.html", {'cart': products, 'cart_total':cart_total})

def add_to_cart(request):
    id = request.POST.get("product_id")
    product = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + 1
    request.session['cart'] = cart

    return redirect('get_products')
    
def remove_from_cart(request):
    id = request.POST.get("product_id")
    phone = get_object_or_404(Product, pk=id)

    cart = request.session.get('cart', {})
    del cart[id]

    request.session['cart'] = cart

    return redirect("cart")