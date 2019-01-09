from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


def home_view(request):
    context = {
        'posts': models.PostModel.objects.all(),
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)


class HomeListView(ListView):
    model = models.PostModel
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


class PostDetailView(DetailView):
    model = models.PostModel


def about_view(request):
    return render(request, 'blog/about.html', {'title': 'About'})
