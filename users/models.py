from django.db import models


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def _str_(self):
        return self.login

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        user_details = UserDetails()
        user_details.user = self
        user_details.save()


class UserDetails(models.Model):
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    sex = models.BooleanField(default=True)
    calories = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='userdetails')

    def _str_(self):
        return self.user
