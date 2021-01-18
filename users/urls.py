from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name="users"),
    path('login/', views.userLogin, name="users"),
    path('<int:pk>', views.user, name="user"),
    path('<int:pk>/details/', views.userDetails, name="user details"),
]