from django.shortcuts import render
from users.models import CustomUser


def register(request):
    return render(request, "user/registration.html")


def confirm_email(request, key):
    return render(request, "user/confirm-email.html", {"key": key, })


def response404(request):
    response = render(request, "404.html")
    return response


def edit_user(request):
    if not request.user.is_authenticated:
        return response404(request)
    current_user = CustomUser.objects.get(pk=request.user.id)
    values = {"first_name": current_user.first_name,
              "last_name": current_user.last_name,
              "user_country": current_user.country.name,
              "pk": current_user.pk, }
    return render(request, "user/edit.html", values)


def login(request):
    return render(request, "user/login.html")


def logout(request):
    return render(request, "user/logout.html")


def meetings(request):
    return render(request, "meetings.html")
