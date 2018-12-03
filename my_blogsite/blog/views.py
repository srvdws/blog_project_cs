from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return HttpResponse('index page')


def about_view(request):
    return HttpResponse('about')
