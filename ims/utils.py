from purchases.models import Purchase
from sales.models import Sale

def calculate_profit():
    total_purchase = Purchase.objects.aggregate(total=models.Sum('total_price'))['total'] or 0
    total_sales = Sale.objects.aggregate(total=models.Sum('total_price'))['total'] or 0

    net_profit = total_sales - total_purchase

    return {
        "total_purchase": total_purchase,
        "total_sales": total_sales,
        "net_profit": net_profit
    }
