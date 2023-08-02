from django.shortcuts import render
from .models import Category
from . import forms
from django.http import HttpResponseRedirect


def index(request):
    categories = Category.objects.all()
    return render(
        request,
        "category/index.html",
        {
            "title": "Category Management",
            "categories": categories,
        },
    )


def create(request):
    category_form = forms.CategoryForm(request.POST or None)

    if request.method == "POST":
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect("/categories/")

    return render(
        request,
        "category/create.html",
        {
            "title": "Create Category",
            "category_form": category_form,
            "error": category_form.errors,
        },
    )


def update(request, category_id):
    category = Category.objects.get(id=category_id)
    category_form = forms.CategoryForm(request.POST or None, instance=category)

    if request.method == "POST":
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect("/categories/")

    return render(
        request,
        "category/create.html",
        {
            "title": "Update Category",
            "category_form": category_form,
            "error": category_form.errors,
        },
    )


def delete(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return HttpResponseRedirect("/categories/")
