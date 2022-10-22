from django.shortcuts import render
from .forms import CreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


User = get_user_model()


class SignUp(CreateView):
    model = User
    form_class = CreationForm
    success_url = reverse_lazy("signup")
    template_name = "signup.html"
