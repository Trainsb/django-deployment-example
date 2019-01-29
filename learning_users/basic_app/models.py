from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    #Fields of the mode. Each field is specified as a class attribute and each attribute maps to a database column. Essentially these are your database inputs without using SQL.

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional classes

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    #Python magic method that returns a string representation of any object.
    def __str__(self):
        return self.user.username
