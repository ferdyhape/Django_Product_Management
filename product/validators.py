from django.core.exceptions import ValidationError


def validate_name(value):
    if value.isdigit():
        raise ValidationError("Name must be a string")


def validate_description(value):
    if value.isdigit():
        raise ValidationError("Description must be a string")


def validate_price(value):
    if value < 0:
        raise ValidationError("Price must be a positive number")


def validate_category(value):
    if value == None:
        raise ValidationError("Category must be selected")
