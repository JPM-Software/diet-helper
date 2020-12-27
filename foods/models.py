from django.db import models
from users.models import User


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=254)
    calories = models.IntegerField()

    def _str_(self):
        return self.name


class DailyDiary(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    foods = models.ManyToManyField(Food)

    def _str_(self):
        return self.user
