from django.shortcuts import render
from purchases.models import Purchase
from sales.models import Sale
from inventory.models import Product


# ---------------------------
# PURCHASE REPORT
# ---------------------------
def purchase_report(request):
    purchases = Purchase.objects.order_by("-created_at")
    return render(request, "reports/purchase_report.html", {"purchases": purchases})

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
    products = Product.objects.all()
    low_stock = products.filter(stock__lt=10)
    return render(request, "reports/stock_report.html", {
        "products": products,
        "low_stock": low_stock
    })




def report_home(request):
    products = Product.objects.all()
    return render(request, "reports/report_home.html", {"products": products})

from django.shortcuts import render
from inventory.models import Product, PurchaseBatch
from sales.models import Sale

def fifo_report(request):
    sales = Sale.objects.all().order_by("-created_at")

    report = []
    for sale in sales:
        report.append({
            "product": sale.product.name,
            "quantity": sale.quantity,
            "selling_price": sale.selling_price,
            "cost_price": sale.cost_price,
            "profit": sale.profit,
            "date": sale.created_at,
        })

    return render(request, "reports/fifo_report.html", {"report": report})
