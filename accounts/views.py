from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def home_page(request):
    return render(request, 'accounts/home.html', {'name': 'Kiran'})


def login_page(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'name': 'Kiran'})

    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect("/home")
    else:
        messages.info(request, "invalid credential......")
        return render(request, 'accounts/login.html', {'name': 'Kiran'})

    return render(request, 'accounts/home.html', {'name': 'Kiran'})


def register_page(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html', {'name': 'Kiran'})

    username = request.POST["username"]
    password1 = request.POST["password"]
    password2 = request.POST["cpassword"]
    email = request.POST["username"]

    if password1 != password2:
        messages.info(request, "Both provided password did not match")
        return render(request, 'accounts/register.html', {'name': 'Kiran'})

    user = User.objects.create_user(
        username=username, email=username, password=password1)
    user.save()
    return redirect("/home")
