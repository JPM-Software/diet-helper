from django.db import models


# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=254)
    calories = models.IntegerField()

    def _str_(self):
        return self.name
