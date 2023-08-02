from django.shortcuts import render
from .models import Category
from django.views import View
from . import forms
from django.http import HttpResponseRedirect


class IndexView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(
            request,
            "category/index.html",
            {
                "title": "Category Management",
                "categories": categories,
            },
        )


class create(View):
    def get(self, request):
        category_form = forms.CategoryForm(request.POST or None)
        return render(
            request,
            "category/create.html",
            {
                "title": "Create Category",
                "category_form": category_form,
                "error": category_form.errors,
            },
        )

    def post(self, request):
        category_form = forms.CategoryForm(request.POST or None)
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


class update(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        category_form = forms.CategoryForm(request.POST or None, instance=category)
        return render(
            request,
            "category/create.html",
            {
                "title": "Update Category",
                "category_form": category_form,
                "error": category_form.errors,
            },
        )

    def post(self, request, category_id):
        category = Category.objects.get(id=category_id)
        category_form = forms.CategoryForm(request.POST or None, instance=category)
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


class delete(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        category.delete()
        return HttpResponseRedirect("/categories/")
