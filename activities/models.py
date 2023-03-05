from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    state = models.CharField(max_length=2)
    activityType = models.CharField(max_length=100)
    description = models.CharField(max_length=4000)
    address = models.CharField(max_length=200)
