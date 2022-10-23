from django.shortcuts import render
from .forms import UserRegistrationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


User = get_user_model()


def SignUp(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'catalog.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'signup.html', {'user_form': user_form})