from django.urls import path
from . import views_function_base
from . import views_class_base
from django.views.generic import TemplateView
from .models import Category

urlpatterns = [
    # path penampilan list category menggunakan template view
    path(
        "categories/",
        TemplateView.as_view(
            template_name="category/index.html",
            extra_context={
                "title": "Category Management",
                "categories": Category.objects.all(),
            },
        ),
        name="categories",
    ),
    # path crud category menggunakan View Class
    path(
        "categories/create/",
        views_class_base.CreateOrUpdateOrDeleteView.as_view(),
        name="create_category",
    ),
    path(
        "categories/update/<int:category_id>/",
        views_class_base.CreateOrUpdateOrDeleteView.as_view(mode="update"),
        name="update_category",
    ),
    path(
        "categories/delete/<int:category_id>/",
        views_class_base.CreateOrUpdateOrDeleteView.as_view(mode="delete"),
        name="delete_category",
    ),
]
