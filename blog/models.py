from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    created_on = models.DateField(auto_now=True)
    descreption = models.CharField(max_length=2550, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)