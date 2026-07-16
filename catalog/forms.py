from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["name", "description", "price", "category", "image"]

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не должна быть отрицательной")
        return price

    def clean_image(self):

        image = self.cleaned_data.get('image')
        if not image:
            return image

        image = self.cleaned_data.get("image")
        max_size = 5 * 1024 * 1024
        if image.size > max_size:
            raise ValidationError("Размер файла не должен превышать 5 МБ.")

        allowed_extensions = ["jpeg", "png"]
        ext = image.name.split(".")[-1].lower()
        if ext not in allowed_extensions:
            raise ValidationError(
                "Допустимы только файлы с расширением .jpeg или .png."
            )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]

        for word in forbidden_words:
            if name and word.lower() in name.lower():
                self.add_error("name", f"Наименование не может содержать слово {word}")

        for word in forbidden_words:
            if description and word.lower() in description.lower():
                self.add_error(
                    "description", f"Описание не может содержать слово {word}"
                )

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название продукта"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )

        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену"}
        )

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-select",
            }
        )

        self.fields["image"].widget.attrs.update(
            {
                "class": "btn-secondary",
            }
        )
