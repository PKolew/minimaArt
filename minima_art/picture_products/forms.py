from django import forms
from .models import Order, Product, Review


class OrderForm(forms.ModelForm):
    size = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter the size you want (e.g., 30x40cm)'})
    )
    wishes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write any special requests here...'}),
    )

    class Meta:
        model = Order
        fields = ['size', 'wishes']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'height', 'width', 'image', 'description', 'category', 'tags', 'stock_quantity', 'sku', 'available']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Product Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'height': forms.NumberInput(attrs={'placeholder': 'Height in cm'}),
            'width': forms.NumberInput(attrs={'placeholder': 'Width in cm'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 4}),
        }