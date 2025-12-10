from django.shortcuts import render
from purchases.models import Purchase
from sales.models import Sale
from inventory.models import Product


# ---------------------------
# PURCHASE REPORT
# ---------------------------
def purchase_report(request):
    purchases = Purchase.objects.select_related("product", "supplier").order_by("-date")
    total_spent = sum(p.total_cost for p in purchases)

    context = {
        "purchases": purchases,
        "total_spent": total_spent,
    }
    return render(request, "reports/purchase_report.html", context)


# ---------------------------
# SALES REPORT
# ---------------------------
def sales_report(request):
    sales = Sale.objects.select_related("product", "customer").order_by("-date")
    total_revenue = sum(s.total_price for s in sales)

    context = {
        "sales": sales,
        "total_revenue": total_revenue,
    }
    return render(request, "reports/sales_report.html", context)


# ---------------------------
# STOCK REPORT
# ---------------------------
def stock_report(request):
    products = Product.objects.all().order_by("name")
    low_stock = products.filter(quantity__lt=10)

    context = {
        "products": products,
        "low_stock": low_stock,
    }
    return render(request, "reports/stock_report.html", context)
