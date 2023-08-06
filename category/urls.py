from django.urls import path
from . import views_class_base
from django.views.generic import TemplateView
from .models import Category
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        "categories/",
        login_required(
            TemplateView.as_view(
                template_name="category/index.html",
                extra_context={
                    "title": "Category Management",
                    "categories": Category.objects.all(),
                },
            )
        ),
        name="categories",
    ),
    path(
        "categories/create/",
        login_required(views_class_base.CreateOrUpdateOrDeleteView.as_view()),
        name="create_category",
    ),
    path(
        "categories/update/<int:category_id>/",
        login_required(
            views_class_base.CreateOrUpdateOrDeleteView.as_view(mode="update")
        ),
        name="update_category",
    ),
    path(
        "categories/delete/<int:category_id>/",
        login_required(
            views_class_base.CreateOrUpdateOrDeleteView.as_view(mode="delete")
        ),
        name="delete_category",
    ),
]
