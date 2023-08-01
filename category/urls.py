from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.index, name="categories"),
    path("categories/create/", views.create, name="create_category"),
    path("categories/update/<int:category_id>/", views.update, name="update_category"),
    path("categories/delete/<int:category_id>/", views.delete, name="delete_category"),
]
