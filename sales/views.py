from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction

from inventory.models import Item
from purchases.models import Purchase
from .models import Sale


def sales_home(request):
    return render(request, "home.html")


@transaction.atomic
def add_sale(request):
    if request.method == "POST":
        item_id = request.POST.get("item")
        quantity = float(request.POST.get("quantity"))
        sale_price = float(request.POST.get("sale_price"))

        # Get selected item
        item = Item.objects.get(id=item_id)

        # Get all Purchase batches with remaining stock for this item (FIFO)
        purchase_batches = Purchase.objects.filter(
            item=item,
            remaining_qty__gt=0
        ).order_by("purchase_date")

        qty_needed = quantity

        for batch in purchase_batches:
            if qty_needed <= 0:
                break

            available = float(batch.remaining_qty)

            if available >= qty_needed:
                batch.remaining_qty = available - qty_needed
                batch.save()
                qty_needed = 0
            else:
                qty_needed -= available
                batch.remaining_qty = 0
                batch.save()

        if qty_needed > 0:
            messages.error(request, "Not enough stock for this sale.")
            return redirect("add_sale")

        # Create sale record
        Sale.objects.create(
            item=item,
            quantity=quantity,
            selling_price_per_unit=sale_price
        )

        messages.success(request, "Sale added successfully.")
        return redirect("sales_list")

    # Load items for dropdown
    items = Item.objects.all()
    return render(request, "sales/add_sale.html", {"items": items})
