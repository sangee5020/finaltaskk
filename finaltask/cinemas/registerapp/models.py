# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    place = models.CharField(max_length=100, blank=True)
