from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PurchaseForm
from .models import Purchase

def add_purchase(request):
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save()
            messages.success(request, "Purchase added successfully!")
            return redirect("add_purchase")
    else:
        form = PurchaseForm()

    return render(request, "purchases/add_purchase.html", {"form": form})
