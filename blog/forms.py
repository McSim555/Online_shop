from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["name", "content", "image", "published"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": ""}),
            "content": forms.Textarea(attrs={"rows": 10}),
        }
