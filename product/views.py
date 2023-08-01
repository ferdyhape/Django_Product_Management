from django.shortcuts import render
from .models import Product
from . import forms
from django.http import HttpResponseRedirect


def index(request):
    products = Product.objects.all()
    return render(
        request,
        "product/index.html",
        {
            "title": "Product Management",
            "products": products,
        },
    )


def create(request):
    product_form = forms.ProductForm(request.POST or None)
    if request.method == "POST":
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect("/products/")

    return render(
        request,
        "product/create.html",
        {
            "title": "Create Product",
            "product_form": product_form,
            "error": product_form.errors,
        },
    )


def update(request, product_id):
    product = Product.objects.get(id=product_id)
    product_form = forms.ProductForm(request.POST or None, instance=product)

    if request.method == "POST":
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect("/products/")

    return render(
        request,
        "product/create.html",
        {
            "title": "Update Product",
            "product_form": product_form,
            "error": product_form.errors,
        },
    )


def delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect("/products/")
