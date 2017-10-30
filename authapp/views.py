from django.shortcuts import render
from django.views import generic
from . import models
from . import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpCreateView(generic.CreateView):
    template_name = "sign_up.html"
    model = models.CustomUser
    form_class = forms.CustomUserForm


def login_view(request):
    pass


def logout_view(request):
    pass