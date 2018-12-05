from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register_view(request):
    print('opened register page')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print('form is created')
        if form.is_valid():
            print('form is valid')
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request, "Account Created for {}".format(username))
            return redirect('home_view')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})
