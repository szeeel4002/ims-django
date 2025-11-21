from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import PurchaseForm
from .models import Purchase
from inventory.models import StockEntry


def add_purchase(request):
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save()

            # Create StockEntry for FIFO
            StockEntry.objects.create(
                purchase=purchase,
                remaining_qty=purchase.quantity
            )

            messages.success(request, "Purchase added and stock updated!")
            return redirect("add_purchase")
    else:
        form = PurchaseForm()

    return render(request, "purchases/add_purchase.html", {"form": form})
