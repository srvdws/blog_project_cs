from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . import forms
from django.contrib.auth.decorators import login_required


def register_view(request):

    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account Created for {}, Please log in.".format(username))
            return redirect('login')
        else:
            messages.warning(request, "Please ensure all information is correct")
            form = forms.UserRegisterForm(request.POST)

    else:
        form = forms.UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile_view(request):

    u_form = forms.UserUpdateForm()
    p_form = forms.ProfileUpdateForm()

    return render(request, 'users/profile.html')
