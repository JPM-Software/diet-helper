from django.urls import path
from . import views

urlpatterns = [
    path('', views.foods, name="foods"),
    path('<str:pk>/', views.food, name="food"),
]