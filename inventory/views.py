
from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, "inventory/home.html")


def dashboard(request):
    return render(request, 'dashboard.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, "inventory/product_list.html", {"products": products})

from django.shortcuts import render, redirect
from .models import Product

def add_product(request):
    if request.method == "POST":
        Product.objects.create(
            name=request.POST["name"],
            price=request.POST["price"],
            stock=request.POST["stock"]
        )
        return redirect("product_list")
    return render(request, "inventory/add_product.html")


def customer_list(request):
    return render(request, 'inventory/customer_list.html')

def supplier_list(request):
    return render(request, 'inventory/supplier_list.html')

def purchase_list(request):
    return render(request, 'inventory/purchase_list.html')

def sales_list(request):
    return render(request, 'inventory/sales_list.html')

# Reports
def purchase_report(request):
    return render(request, 'reports/purchase_report.html')

def sales_report(request):
    return render(request, 'reports/sales_report.html')

def stock_report(request):
    return render(request, 'reports/stock_report.html')
