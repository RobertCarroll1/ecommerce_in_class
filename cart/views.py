from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from products.models import Product

# Create your views here.
def get_cart(request):
    cart = request.session.get('cart', {})

    products = []
    for p in cart:
        product = get_object_or_404(Product, pk=p)

        products.append({
            'product': product,
            'quantity': cart[p],
            'total': product.price * quantity
    })

    cart_total += phone.price * quantity


        # products.append((phone, cart[p]))

    return render(request, "cart/cart.html", {'cart': products})

def add_to_cart(request):
    id = request.POST.get("product_id")
    phone = get_object_or_404(Product, pk=id)

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + 1

    request.session['cart'] = cart

    return HttpResponse(cart[id])
    
def remove_from_cart(request):
    id = request.POST.get("product_id")
    phone = get_object_or_404(Product, pk=id)

    cart = request.session.get('cart', {})
    del cart[id]

    request.session['cart'] = cart

    return redirect("cart")