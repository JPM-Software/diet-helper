from django.db import models


# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=254)
    calories = models.IntegerField(max_length=254)

    def _str_(self):
        return self.name
