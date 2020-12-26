from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name="users"),
    path('<str:pk>/', views.user, name="user"),
    path('<str:pk>/details/', views.userDetails, name="user details"),
]