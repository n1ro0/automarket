from django.shortcuts import render, redirect
from django.views import generic
from . import models
from . import forms
from django.contrib.auth import authenticate, login, logout
from urllib.parse import parse_qs
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView


class SignUpCreateView(generic.CreateView):
    template_name = "sign_up.html"
    model = models.CustomUser
    form_class = forms.CustomUserCreationForm
    success_url = "/"

class MyLoginView(LoginView):
    template_name = 'login.html'


class MyLogoutView(LogoutView):
    pass


def login_view(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            qs = parse_qs(request.environ['QUERY_STRING'])
            return redirect(qs.get('next', ['/'])[0])
        else:
            return render(request, 'error_login.html')
    if (request.method == "GET"):
        if not request.user.is_authenticated:
            form = forms.AuthenticationForm
            return render(request, 'login.html', context={'form': form})
        else:
            return render(request, "logout.html")



def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    elif request.method == "GET":
        if not request.user.is_authenticated:
            return render(request, 'not_logedin.html')
        else:
            return render(request, "logout.html")