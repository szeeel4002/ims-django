from django.shortcuts import render, redirect, get_object_or_404
from .models import Purchase
from .forms import PurchaseForm
from inventory.models import Product, Supplier


def purchase_list(request):
    purchases = Purchase.objects.all().order_by("-created_at")
    return render(request, "purchases/purchase_list.html", {"purchases": purchases})


def add_purchase(request):
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("purchase_list")
    else:
        form = PurchaseForm()

    return render(request, "purchases/add_purchase.html", {"form": form})


def edit_purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id)
    form = PurchaseForm(request.POST or None, instance=purchase)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("purchase_list")

    return render(request, "purchases/edit_purchase.html", {
        "form": form,
        "purchase": purchase,
        "products": Product.objects.all(),
        "suppliers": Supplier.objects.all(),
    })


def delete_purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id)

    if request.method == "POST":
        purchase.delete()
        return redirect("purchase_list")

    return render(request, "purchases/delete_purchase.html", {"purchase": purchase})
