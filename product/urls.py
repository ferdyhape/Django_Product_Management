from django.urls import path
from . import views
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path("products/", views.index, name="products"),
    path(
        "products/",
        login_required(
            ListView.as_view(
                template_name="product/index.html",
                model=views.Product,
                extra_context={
                    "title": "Product Management",
                },
            ),
        ),
        name="products",
    ),
    path("products/create/", login_required(views.create), name="create_product"),
    path(
        "products/update/<int:product_id>/",
        login_required(views.update),
        name="update_product",
    ),
    path(
        "products/delete/<int:product_id>/",
        login_required(views.delete),
        name="delete_product",
    ),
    path(
        "product/<str:category_name>/",
        login_required(views.product_by_category),
        name="product_by_category",
    ),
]
