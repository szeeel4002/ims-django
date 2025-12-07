from django.db.models import F
from inventory.models import Product

def low_stock_context(request):
    try:
        low_stock_products = Product.objects.filter(
            quantity__lte=F("low_stock_limit")
        )
        return {
            "low_stock_count": low_stock_products.count(),
            "low_stock_sample": low_stock_products[:5],
        }
    except Exception:
        # In case of migrations / no table yet
        return {"low_stock_count": 0, "low_stock_sample": []}
