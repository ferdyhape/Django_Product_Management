from django.db import models
from . import validators


class Product(models.Model):
    name = models.CharField(
        max_length=255, unique=True, validators=[validators.validate_name]
    )
    description = models.TextField(validators=[validators.validate_description])
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[validators.validate_price]
    )
    category = models.ForeignKey(
        "category.Category",
        on_delete=models.CASCADE,
        validators=[validators.validate_category],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.category.name}"

    class Meta:
        db_table = "products"
