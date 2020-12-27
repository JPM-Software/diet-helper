from django.urls import path
from . import views

urlpatterns = [
    path('', views.diaries, name="diaries"),
    path('<str:pk>/', views.diary, name="diary"),
    path('foods/all', views.foods, name="foods"),
    path('foods/<str:pk>/', views.food, name="food"),
    path('<str:pk>/foods/', views.foods_for_diary, name="foods for diary"),
]