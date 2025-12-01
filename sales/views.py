from django.shortcuts import render, redirect
from django.contrib import messages
from inventory.models import Product
from .models import Sale

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Sale
from inventory.models import Product

def sales_home(request):
    return render(request, "sales/sales_home.html")



def add_sale(request):
    if request.method == "POST":
        product_id = request.POST.get("product")
        quantity = int(request.POST.get("quantity"))
        price = float(request.POST.get("sale_price"))

        product = Product.objects.get(id=product_id)

        if product.stock < quantity:
            messages.error(request, "Not enough stock!")
            return redirect("add_sale")

        product.stock -= quantity
        product.save()

        Sale.objects.create(product=product, quantity=quantity, sale_price=price)

        messages.success(request, "Sale recorded successfully!")
        return redirect("add_sale")

    products = Product.objects.all()
    return render(request, "sales/add_sale.html", {"products": products})

def sales_home(request):
    return render(request, "sales/home.html")
