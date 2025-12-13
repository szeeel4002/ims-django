from django.shortcuts import render, redirect, get_object_or_404
from .models import Purchase
from inventory.models import Product, Supplier
from inventory.models import Product, PurchaseBatch

def purchase_list(request):
    purchases = Purchase.objects.all().order_by("-created_at")
    return render(request, "purchases/purchase_list.html", {"purchases": purchases})

def add_purchase(request):
    if request.method == "POST":
        product = Product.objects.get(id=request.POST["product"])
        qty = int(request.POST["quantity"])
        price = float(request.POST["price"])

        Purchase.objects.create(
            product=product,
            quantity=qty,
            price_per_unit=price
        )

        PurchaseBatch.objects.create(
            product=product,
            quantity_left=qty,
            price_per_unit=price
        )

        product.stock += qty
        product.save()

        return redirect("purchase_list")

    products = Product.objects.all()
    return render(request, "purchases/add_purchase.html", {"products": products})


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
