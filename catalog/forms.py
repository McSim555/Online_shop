from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']
        # или '__all__', если хотите все поля, но лучше перечислить явно.
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': ''}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
