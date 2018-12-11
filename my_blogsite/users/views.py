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

    if request.method == 'POST':
        u_form = forms.UserUpdateForm(request.POST, instance = request.user)
        p_form = forms.ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, "account updated")
            return redirect('profile')
        else:
            u_form = forms.UserUpdateForm(instance=request.user)
            p_form = forms.ProfileUpdateForm(instance=request.user.profilemodel)
    else:
        u_form = forms.UserUpdateForm(instance=request.user)
        p_form = forms.ProfileUpdateForm(instance=request.user.profilemodel)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)
