from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name = "index_view"),
    path('about/', views.about_view, name = "about_view" )
]
