from django import forms
from .models import Product


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Поиск')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []