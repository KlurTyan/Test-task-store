from django.shortcuts import render, get_object_or_404

from .models import Item
from cart.forms import CartAddItemForm

def item_list(request):
    items = Item.objects.all()
    return render(request, "./store/product/list.html", {"items": items})

def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    cart_product_form = CartAddItemForm()
    return render(request, "./store/product/detail.html", {"item": item, 'cart_product_form': cart_product_form})