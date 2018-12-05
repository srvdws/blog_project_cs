from django.shortcuts import render
from . import models


def home_view(request):
    context = {
        'posts': models.PostModel.objects.all(),
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)


def about_view(request):
    return render(request, 'blog/about.html', {'title': 'About'})
