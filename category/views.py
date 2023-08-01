from django.shortcuts import render


def index(request):
    return render(
        request,
        "category/index.html",
        {
            "title": "Category Management",
        },
    )
