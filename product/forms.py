from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "category", "image"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Product Name",
                    "id": "name",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Product Description",
                    "id": "description",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Product Price",
                    "id": "price",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Product Category",
                    "id": "category",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Product Image",
                    "id": "image",
                }
            ),
        }
