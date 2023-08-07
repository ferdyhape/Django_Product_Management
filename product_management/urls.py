from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView, RedirectView
from . import views
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.conf.urls.static import static


def is_not_authenticated(user):
    return not user.is_authenticated


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "home/",
        RedirectView.as_view(
            url="/",
            permanent=False,
        ),
        name="home_redirect",
    ),
    path(
        "",
        TemplateView.as_view(
            template_name="static_html/home.html",
            extra_context={
                "title": "Home",
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
    path(
        "login/",
        user_passes_test(is_not_authenticated, login_url=reverse_lazy("home"))(
            views.LoginView.as_view()
        ),
        name="login",
    ),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("", include("product.urls")),
    path("", include("category.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
