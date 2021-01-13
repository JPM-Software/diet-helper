from django.urls import path
from . import views

urlpatterns = [
    path('', views.diaries, name="diaries"),
    path('<int:pk>', views.diary, name="diary"),
    path('foods/', views.foods, name="foods"),
    path('foods/<int:pk>', views.food, name="food"),
    path('<int:pk>/foods/', views.foods_for_diary, name="foods for diary"),
    path('by-user/<int:pk>', views.diaries_by_user, name="diaries by user id"),
    path('by-user/<int:pk>/today/', views.diaries_by_user_today, name="today diary by user id"),
]