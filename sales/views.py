from django.shortcuts import render, redirect, get_object_or_404
from .models import Sale
from .forms import SaleForm
from inventory.models import Customer, Product


def sale_list(request):
    sales = Sale.objects.all().order_by("-date")
    return render(request, "sales/sale_list.html", {"sales": sales})


def add_sale(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save()
            return redirect("sale_invoice", sale_id=sale.id)
    else:
        form = SaleForm()

    return render(request, "sales/add_sale.html", {
        "form": form,
        "customers": Customer.objects.all(),
        "products": Product.objects.all(),
    })


def edit_sale(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    form = SaleForm(request.POST or None, instance=sale)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("sale_list")

    return render(request, "sales/edit_sales.html", {
        "form": form,
        "sale": sale,
        "customers": Customer.objects.all(),
        "products": Product.objects.all(),
    })


def delete_sale(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)

    if request.method == "POST":
        sale.delete()
        return redirect("sale_list")

    return render(request, "sales/delete_sales.html", {"sale": sale})


def sale_invoice(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    return render(request, "sales/invoice_template.html", {"sale": sale})
