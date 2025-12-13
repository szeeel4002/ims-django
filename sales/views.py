from django.shortcuts import render, redirect, get_object_or_404
from .models import Sale
from .forms import SaleForm
from inventory.models import Customer, Product

def sales_list(request):
    sales = Sale.objects.all().order_by("-created_at")
    return render(request, "sales/sales_list.html", {"sales": sales})




def add_sale(request):
    if request.method == "POST":
        product = Product.objects.get(id=request.POST["product"])
        qty = int(request.POST["quantity"])

        if product.stock < qty:
            return render(request, "sales/error.html")

        Sale.objects.create(
            product=product,
            quantity=qty,
            price=request.POST["price"]
        )

        product.stock -= qty
        product.save()

        return redirect("sales_list")

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
