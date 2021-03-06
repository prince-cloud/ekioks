from .models import Product, ProductImages
from django import forms

class Sellform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'brand', 'description', 
        'condition', 'price', 'image', 'phone', 'region',]
