from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Customer, Supplier
from .forms import CustomerForm, SupplierForm

# ===========================
#       DASHBOARD VIEW
# ===========================
def dashboard(request):
    return render(request, "dashboard.html")


# ===========================
#       CUSTOMERS
# ===========================
def customer_list(request):
    customers = Customer.objects.all().order_by("name")
    return render(request, "inventory/customer_list.html", {"customers": customers})


def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer added successfully!")
            return redirect("customer_list")
    else:
        form = CustomerForm()
    return render(request, "inventory/customer_form.html", {"form": form, "title": "Add Customer"})


def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer updated successfully!")
            return redirect("customer_list")
    else:
        form = CustomerForm(instance=customer)
    return render(request, "inventory/customer_form.html", {"form": form, "title": "Edit Customer"})


def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == "POST":
        customer.delete()
        messages.success(request, "Customer deleted!")
        return redirect("customer_list")
    return render(request, "inventory/customer_confirm_delete.html", {"customer": customer})


# ===========================
#       SUPPLIERS
# ===========================
def supplier_list(request):
    suppliers = Supplier.objects.all().order_by("name")
    return render(request, "inventory/supplier_list.html", {"suppliers": suppliers})


def add_supplier(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier added successfully!")
            return redirect("supplier_list")
    else:
        form = SupplierForm()
    return render(request, "inventory/supplier_form.html", {"form": form, "title": "Add Supplier"})


def edit_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier updated successfully!")
            return redirect("supplier_list")
    else:
        form = SupplierForm(instance=supplier)
    return render(request, "inventory/supplier_form.html", {"form": form, "title": "Edit Supplier"})


def delete_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == "POST":
        supplier.delete()
        messages.success(request, "Supplier deleted!")
        return redirect("supplier_list")
    return render(request, "inventory/supplier_confirm_delete.html", {"supplier": supplier})
