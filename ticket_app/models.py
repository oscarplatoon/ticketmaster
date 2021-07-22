from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  active = models.BooleanField(default=True)


# class Event(models.Model):
#   name = models.CharField(max_length=200)
#   date = models.DateTimeField()
#   description = models.TextField(max_length=1000)
#   image_url = models.CharField(max_length=250)

#   def __str__(self):
#       return f"{self.name}"

# class Event(models.Model):
#     def __init__(self, json):
#         self.id = json['id']
#         self.name = json['name']
#         self.images = json['images']
#         self.dates = json['dates']