from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.views import View
from django.contrib.auth.models import User


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


class RegisterView(View):
    template_name = "static_html/auth/register.html"

    def get(self, request):
        context = {
            "title": "Register",
        }
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        email = request.POST.get("email")

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            context = {"title": "Register", "error_message": "Username already exists"}
            return render(request, self.template_name, context)

        # Create a new user object
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email,
        )

        # Save the user object
        user.save()

        # Redirect the user to a success page or any desired URL
        return HttpResponseRedirect(
            "/login"
        )  # Replace "home" with the desired URL name


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
