from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "home/",
        RedirectView.as_view(
            url="/",
            permanent=False,
        ),
    ),
    path(
        "",
        TemplateView.as_view(
            template_name="static_html/home.html",
            extra_context={
                "title": "Home",
                "message": "Welcome to Product Management",
            },
        ),
        name="home",
    ),
    path(
        "about/",
        TemplateView.as_view(
            template_name="static_html/about.html",
            extra_context={
                "title": "About",
                "message": "This is a simple Django project for managing products",
            },
        ),
        name="about",
    ),
    path("", include("product.urls")),
    path("", include("category.urls")),
]
