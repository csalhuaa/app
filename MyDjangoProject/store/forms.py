from django import forms

from .models.Category import Category

class ProductFilterForm(forms.Form):
    name = forms.CharField(required=False)
    min_price = forms.DecimalField(required=False)
    max_price = forms.DecimalField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
