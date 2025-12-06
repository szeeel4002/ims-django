from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SaleForm
from inventory.models import Product
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from .models import Sale
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Sale



def add_sale(request):
    if request.method == "POST":
        form = SaleForm(request.POST)

        if form.is_valid():
            sale = form.save(commit=False)

            quantity = form.cleaned_data['quantity']
            price_per_unit = form.cleaned_data['price_per_unit']

            # Auto calculate total
            sale.total_price = quantity * price_per_unit

            # Validate stock
            product = sale.product
            if quantity > product.quantity:
                messages.error(
                    request,
                    f"Not enough stock! Available: {product.quantity}"
                )
                return redirect("add_sale")

            # Reduce stock
            product.quantity -= quantity
            product.save()

            sale.save()
            messages.success(request, "Sale recorded successfully!")
            return redirect("sale_list")

    else:
        form = SaleForm()

    return render(request, "sales/add_sale.html", {"form": form})


def sale_list(request):
    from .models import Sale
    sales = Sale.objects.select_related("product").order_by("-date")
    return render(request, "sales/sale_list.html", {"sales": sales})



def generate_invoice(request, sale_id):
    sale = Sale.objects.get(id=sale_id)

    html = render_to_string("sales/invoice_template.html", {"sale": sale})

    pdf = pdfkit.from_string(html, False)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{sale_id}.pdf"'

    return response
