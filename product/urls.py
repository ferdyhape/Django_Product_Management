from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.index, name="products"),
    path("products/create/", views.create, name="create_product"),
    path("products/update/<int:product_id>/", views.update, name="update_product"),
    path("products/delete/<int:product_id>/", views.delete, name="delete_product"),
    path(
        "product/<str:category_name>/",
        views.product_by_category,
        name="product_by_category",
    ),
]
