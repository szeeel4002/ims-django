from django.shortcuts import render
from django.http import HttpResponse
from django.utils.dateparse import parse_date
from sales.models import Sale
from purchases.models import Purchase
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import csv

def sales_report(request):
    start = request.GET.get("start")
    end = request.GET.get("end")
    export = request.GET.get("export")  # 'csv' or 'pdf'

    sales = Sale.objects.all().order_by("-date")

    if start:
        sales = sales.filter(date__gte=parse_date(start))
    if end:
        sales = sales.filter(date__lte=parse_date(end))

    # CSV EXPORT
    if export == "csv":
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="sales_report.csv"'
        writer = csv.writer(response)
        writer.writerow(["Date", "Product", "Customer", "Qty", "Price/Unit", "Total"])
        for s in sales:
            writer.writerow([s.date, s.product.name, str(s.customer), s.quantity, s.price_per_unit, s.total_price])
        return response

    # PDF EXPORT (simple)
    if export == "pdf":
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="sales_report.pdf"'
        p = canvas.Canvas(response, pagesize=A4)
        width, height = A4

        y = height - 50
        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, y, "Sales Report")
        y -= 30
        p.setFont("Helvetica", 10)
        for s in sales:
            line = f"{s.date} | {s.product.name} | {s.customer} | Qty: {s.quantity} | Total: {s.total_price}"
            p.drawString(50, y, line[:110])
            y -= 15
            if y < 50:
                p.showPage()
                y = height - 50
        p.showPage()
        p.save()
        return response

    return render(request, "reports/sales_report.html", {"sales": sales, "start": start, "end": end})


def purchase_report(request):
    start = request.GET.get("start")
    end = request.GET.get("end")
    export = request.GET.get("export")

    purchases = Purchase.objects.all().order_by("-date")

    if start:
        purchases = purchases.filter(date__gte=parse_date(start))
    if end:
        purchases = purchases.filter(date__lte=parse_date(end))

    if export == "csv":
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="purchase_report.csv"'
        writer = csv.writer(response)
        writer.writerow(["Date", "Product", "Supplier", "Qty", "Price/Unit", "Total"])
        for p_obj in purchases:
            writer.writerow([p_obj.date, p_obj.product.name, str(p_obj.supplier), p_obj.quantity, p_obj.price_per_unit, p_obj.total_price])
        return response

    if export == "pdf":
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="purchase_report.pdf"'
        p = canvas.Canvas(response, pagesize=A4)
        width, height = A4

        y = height - 50
        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, y, "Purchase Report")
        y -= 30
        p.setFont("Helvetica", 10)
        for po in purchases:
            line = f"{po.date} | {po.product.name} | {po.supplier} | Qty: {po.quantity} | Total: {po.total_price}"
            p.drawString(50, y, line[:110])
            y -= 15
            if y < 50:
                p.showPage()
                y = height - 50
        p.showPage()
        p.save()
        return response

    return render(request, "reports/purchase_report.html", {"purchases": purchases, "start": start, "end": end})
