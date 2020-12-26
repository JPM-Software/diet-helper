from django.db import models

# Create your models here.

class User(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def _str_(self):
        return self.login