from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import SaleForm
from .models import Sale
from inventory.models import Product

def generate_invoice(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)

    gst_rate = 18  # 18% GST
    gst_amount = sale.total_price * gst_rate / 100
    grand_total = sale.total_price + gst_amount

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="invoice_{sale_id}.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    y = height - 50
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Invoice")
    y -= 30

    p.setFont("Helvetica", 10)
    p.drawString(50, y, f"Invoice No: {sale.id}")
    y -= 15
    p.drawString(50, y, f"Date: {sale.date}")
    y -= 30

    p.drawString(50, y, f"Customer: {sale.customer}")
    y -= 30

    p.drawString(50, y, f"Product: {sale.product.name}")
    y -= 15
    p.drawString(50, y, f"Quantity: {sale.quantity}")
    y -= 15
    p.drawString(50, y, f"Price/Unit: ₹ {sale.price_per_unit}")
    y -= 15
    p.drawString(50, y, f"Subtotal: ₹ {sale.total_price}")
    y -= 20

    p.setFont("Helvetica-Bold", 11)
    p.drawString(50, y, f"GST @ {gst_rate}%: ₹ {gst_amount:.2f}")
    y -= 20
    p.drawString(50, y, f"Grand Total: ₹ {grand_total:.2f}")
    y -= 40

    p.setFont("Helvetica", 9)
    p.drawString(50, y, "Thank you for your business!")

    p.showPage()
    p.save()
    return response


def add_sale(request):
    if request.method == "POST":
        form = SaleForm(request.POST)

        if form.is_valid():
            sale = form.save(commit=False)

            quantity = form.cleaned_data['quantity']
            price_per_unit = form.cleaned_data['price_per_unit']

            sale.total_price = quantity * price_per_unit

            sale.save()
            messages.success(request, "Sale added successfully!")
            return redirect("sale_list")

    else:
        form = SaleForm()

    return render(request, "sales/add_sale.html", {"form": form})


def sale_list(request):
    sales = Sale.objects.select_related("customer").order_by("-date")
    return render(request, "sales/sale_list.html", {"sales": sales})


def edit_sale(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)

    if request.method == "POST":
        form = SaleForm(request.POST, instance=sale)

        if form.is_valid():
            updated_sale = form.save(commit=False)

            updated_sale.total_price = (
                updated_sale.quantity * updated_sale.price_per_unit
            )

            updated_sale.save()
            messages.success(request, "Sale updated successfully!")
            return redirect("sale_list")

    else:
        form = SaleForm(instance=sale)

    return render(request, "sales/edit_sale.html", {"form": form, "sale": sale})


def delete_sale(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)

    if request.method == "POST":
        sale.delete()
        messages.success(request, "Sale deleted successfully!")
        return redirect("sale_list")

    return render(request, "sales/delete_sale.html", {"sale": sale})
