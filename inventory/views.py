from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def product_list(request):
    return render(request, 'inventory/product_list.html')

def add_product(request):
    return render(request, 'inventory/add_product.html')

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
