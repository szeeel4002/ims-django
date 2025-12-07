from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PurchaseForm
from .models import Purchase
from inventory.models import Product
from django.shortcuts import render, redirect, get_object_or_404



def add_purchase(request):
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)

            # Get cleaned data
            quantity = form.cleaned_data['quantity']
            price_per_unit = form.cleaned_data['price_per_unit']

            # Auto calculate total price
            purchase.total_price = quantity * price_per_unit

            purchase.save()

            # -----------------------------
            # AUTO STOCK UPDATE (Increase)
            # -----------------------------
            product = purchase.product
            product.quantity += quantity
            product.save()

            messages.success(request, "Purchase added successfully! Stock updated.")
            return redirect("purchase_list")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PurchaseForm()

    return render(request, "purchases/add_purchase.html", {"form": form})


def purchase_list(request):
    purchases = Purchase.objects.select_related("product").order_by("-date")
    return render(request, "purchases/purchase_list.html", {"purchases": purchases})

def edit_purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id)

    old_quantity = purchase.quantity  # store old quantity to update stock later

    if request.method == "POST":
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            updated_purchase = form.save(commit=False)

            # Update total price
            updated_purchase.total_price = (
                updated_purchase.quantity * updated_purchase.price_per_unit
            )
            updated_purchase.save()

            # Update stock effect
            diff = updated_purchase.quantity - old_quantity
            purchase.product.quantity += diff
            purchase.product.save()

            messages.success(request, "Purchase updated successfully!")
            return redirect("purchase_list")
    else:
        form = PurchaseForm(instance=purchase)

    return render(request, "purchases/edit_purchase.html", {"form": form})
def delete_purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id)

    # Restore stock before deleting
    purchase.product.quantity -= purchase.quantity
    purchase.product.save()

    purchase.delete()
    messages.success(request, "Purchase deleted successfully!")
    return redirect("purchase_list")
