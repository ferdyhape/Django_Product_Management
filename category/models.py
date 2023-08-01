from django.db import models
from . import validators


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        validators=[validators.validate_name, validators.validate_description],
    )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "categories"
