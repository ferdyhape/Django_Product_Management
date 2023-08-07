from django.shortcuts import render, get_object_or_404
from .models import Product
from . import forms
from django.views import View
from django.http import HttpResponseRedirect
import uuid
import os


def create(request):
    if request.method == "POST":
        product_form = forms.ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save(commit=False)

            if "image" in request.FILES:
                random_image_name = str(uuid.uuid4())
                image_extension = str(request.FILES["image"]).split(".")[-1].lower()
                new_image_name = f"{random_image_name}.{image_extension}"
                product.image.name = new_image_name

            product_form.save()
            return HttpResponseRedirect("/products/")
    else:
        product_form = forms.ProductForm()

    context = {
        "title": "Create Product",
        "product_form": product_form,
        "error": product_form.errors,
    }
    return render(request, "product/create.html", context)


def update(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        product_form = forms.ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            updated_product = product_form.save(commit=False)

            if "image" in request.FILES:
                random_image_name = str(uuid.uuid4())
                image_extension = str(request.FILES["image"]).split(".")[-1].lower()
                new_image_name = f"{random_image_name}.{image_extension}"
                updated_product.image.name = new_image_name

            updated_product.save()
            return HttpResponseRedirect("/products/")
    else:
        product_form = forms.ProductForm(instance=product)

    context = {
        "title": "Update Product",
        "product_form": product_form,
        "error": product_form.errors,
    }
    return render(request, "product/create.html", context)


def delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.image.delete()
    product.delete()
    return HttpResponseRedirect("/products/")


def product_by_category(request, category_name):
    products = Product.objects.filter(category__name=category_name)
    print(products)
    return render(
        request,
        "product/index.html",
        {
            "title": "Product Management",
            "object_list": products,
        },
    )
