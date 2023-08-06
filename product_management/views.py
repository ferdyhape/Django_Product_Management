from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.views import View


class LoginView(View):
    template_name = "static_html/auth/login.html"

    def get(self, request):
        context = {
            "title": "Login",
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/products/")
        else:
            context = {
                "title": "Login",
                "error": "Username or password is incorrect",
            }
            return render(request, self.template_name, context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
