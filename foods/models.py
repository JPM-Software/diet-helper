from django.db import models
from users.models import User
from datetime import date


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=254)
    calories = models.IntegerField()

    def _str_(self):
        return self.name


class DailyDiary(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #date = models.DateField(auto_now_add=True)
    date = models.DateField(default=date.today(), blank=True)
    foods = models.ManyToManyField(Food, null=True, blank=True)

    def _str_(self):
        return self.user
