from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render
from inventory.models import Item
from purchases.models import Purchase
from sales.models import Sale
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignupForm, LoginForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})



def home(request):
    return HttpResponse("<h1>Welcome to Inventory Management System</h1>")

def home(request):
    return redirect("/accounts/login/")

def home(request):
    last_login = request.session.get("last_login_time", "First Login")
    return render(request, "home.html", {"last_login": last_login})



def home(request):
    context = {
        "total_items": Item.objects.count(),
        "total_purchases": Purchase.objects.count(),
        "total_sales": Sale.objects.count(),

        "recent": [
            {
                "item": p.item.name,
                "type": "Purchase",
                "quantity": p.quantity,
                "date": p.purchase_date,
            } for p in Purchase.objects.order_by("-id")[:5]
        ] + [
            {
                "item": s.item.name,
                "type": "Sale",
                "quantity": s.quantity,
                "date": s.sale_date,
            } for s in Sale.objects.order_by("-id")[:5]
        ],
    }

    return render(request, "dashboard.html", context)
