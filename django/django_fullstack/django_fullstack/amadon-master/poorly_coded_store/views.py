from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all(),
    }
    return render(request, "store/index.html", context)

def process(request):
    quantity_from_form = int(request.POST["quantity"])
    request.session['q_f_f'] = quantity_from_form 
    print(quantity_from_form)
    request.session['item_id'] = request.POST['price']
    get_item_price = Product.objects.filter(id = request.session['item_id'])
    print(get_item_price[0].price, '/*' *15)
    price_item = get_item_price[0].price
    price_from_form = float(price_item)
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...", '*/' *15)
    
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    
    return redirect("/checkout")

def checkout(request):
    get_item_price = Product.objects.filter(id = request.session['item_id'])
    price_item = get_item_price[0].price
    price_from_form = float(price_item)
    total_charge = request.session['q_f_f'] * price_from_form
    context = {
        "prices": Order.objects.all(),
        'total_charge': total_charge,
        'quantity': request.session['q_f_f'],
    }

    return render(request, "store/checkout.html",context)