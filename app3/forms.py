from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'customer_name', 'customer_email', 'quantity']
        widgets = {
            'product': forms.HiddenInput(),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
