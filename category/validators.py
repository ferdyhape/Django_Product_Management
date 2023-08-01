from django.core.exceptions import ValidationError


def validate_name(value):
    if value == "Alcohol":
        raise ValidationError("Name cannot be Alcohol")


def validate_description(value):
    if value.isdigit():
        raise ValidationError("Description cannot be numeric")
