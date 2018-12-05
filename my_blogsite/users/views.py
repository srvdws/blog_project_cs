from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . import forms


def register_view(request):

    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account Created for {}".format(username))
            return redirect('home_view')
        else:
            messages.warning(request, "Please ensure all information is correct")
            form = forms.UserRegisterForm(request.POST)

    else:
        form = forms.UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
