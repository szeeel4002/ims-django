from django import forms
from .models import Purchase
from inventory.models import Item

class PurchaseForm(forms.ModelForm):
    item = forms.ModelChoiceField(
        queryset=Item.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Purchase
        fields = ["item", "quantity", "cost_price", "purchase_date"]
        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "cost_price": forms.NumberInput(attrs={"class": "form-control"}),
            "purchase_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }
