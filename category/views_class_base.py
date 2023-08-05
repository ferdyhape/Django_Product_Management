from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Category
from django.views import View
from . import forms
from django.http import HttpResponseRedirect


class CreateOrUpdateOrDeleteView(View):
    template_name = "category/create.html"
    form_class = forms.CategoryForm
    mode = None

    # apabila mode request adalah get
    def get(self, request, *args, **kwargs):
        # apabila mode update
        if self.mode == "update" and "category_id" in kwargs:
            category = get_object_or_404(Category, id=kwargs["category_id"])
            initial_data = category.__dict__
            category_form = self.form_class(initial=initial_data, instance=category)
            context = {
                "title": "Update Category",
                "category_form": category_form,
            }
            return render(request, self.template_name, context)

        # apabila mode delete
        elif self.mode == "delete" and "category_id" in kwargs:
            category = get_object_or_404(Category, id=kwargs["category_id"])
            category.delete()
            return HttpResponseRedirect("/categories/")

        # apabila tanpa inisiasi mode, berarti create
        else:
            context = {
                "title": "Create Category",
                "category_form": self.form_class(),
            }
            return render(request, self.template_name, context)

    # apabila mode request adalah post
    def post(self, request, *args, **kwargs):
        # apabila terdapat category_id di kwargs, maka update category
        if "category_id" in kwargs:
            category = get_object_or_404(Category, id=kwargs["category_id"])
            form = self.form_class(request.POST, instance=category)

        # apabila tidak terdapat category_id di kwargs, maka create category
        else:
            form = self.form_class(request.POST)

        # apabila form valid, maka save form
        if form.is_valid():
            form.save()

        return HttpResponseRedirect("/categories/")
