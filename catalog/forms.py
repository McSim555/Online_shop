from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': ''}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не должна быть отрицательной')
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар' ]

        for word in forbidden_words:
            if name and word.lower() in name.lower():
                self.add_error('name', f'Наименование не может содержать слово {word}')

        for word in forbidden_words:
            if description and word.lower() in description.lower():
                self.add_error('name', f'Описание не может содержать слово {word}')



