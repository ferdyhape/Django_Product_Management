from django.urls import path
from . import views_function_base
from . import views_class_base

urlpatterns = [
    # path("categories/", views_function_base.index, name="categories"),
    # path("categories/create/", views_function_base.create, name="create_category"),
    # path(
    #     "categories/update/<int:category_id>/",
    #     views_function_base.update,
    #     name="update_category",
    # ),
    # path(
    #     "categories/delete/<int:category_id>/",
    #     views_function_base.delete,
    #     name="delete_category",
    # ),
    path("categories/", views_class_base.IndexView.as_view(), name="categories"),
    path(
        "categories/create/", views_class_base.create.as_view(), name="create_category"
    ),
    path(
        "categories/update/<int:category_id>/",
        views_class_base.update.as_view(),
        name="update_category",
    ),
    path(
        "categories/delete/<int:category_id>/",
        views_class_base.delete.as_view(),
        name="delete_category",
    ),
]
