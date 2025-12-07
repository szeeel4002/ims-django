from django.shortcuts import render
from inventory.models import Product
from sales.models import Sale
from purchases.models import Purchase
from django.db.models import Sum, F

def dashboard(request):
    total_products = Product.objects.count()
    total_stock_units = Product.objects.aggregate(
        total=Sum("quantity")
    )["total"] or 0

    total_sales_amount = Sale.objects.aggregate(
        total=Sum("total_price")
    )["total"] or 0

    total_purchase_amount = Purchase.objects.aggregate(
        total=Sum("total_price")
    )["total"] or 0

    low_stock_items = Product.objects.filter(quantity__lte=F("low_stock_limit"))

    recent_sales = Sale.objects.select_related("product", "customer").order_by("-date")[:5]
    recent_purchases = Purchase.objects.select_related("product", "supplier").order_by("-date")[:5]

    context = {
        "total_products": total_products,
        "total_stock_units": total_stock_units,
        "total_sales_amount": total_sales_amount,
        "total_purchase_amount": total_purchase_amount,
        "low_stock_items": low_stock_items,
        "recent_sales": recent_sales,
        "recent_purchases": recent_purchases,
    }

    return render(request, "dashboard.html", context)
