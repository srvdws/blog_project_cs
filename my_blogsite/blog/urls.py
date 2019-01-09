from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeListView.as_view(), name = "home_view"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name = "post_detail"),
    path('about/', views.about_view, name = "about_view" )
]
