from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser

class UserToken(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     token = models.OneToOneField(Token,on_delete=models.CASCADE)


