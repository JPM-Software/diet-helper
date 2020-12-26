from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('users/', views.users, name="users"),
    path('user/<str:pk>/', views.user, name="user"),
]