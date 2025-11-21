from django import forms
from .models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ["item_name", "quantity", "cost_price", "purchase_date"]
        widgets = {
            "purchase_date": forms.DateInput(attrs={"type": "date"})
        }
