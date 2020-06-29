from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    group_code = models.IntegerField()
    description = models.TextField()
    image_link = models.TextField()

    def __str__(self):
        return self.name

class WeightLog(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    weight = models.CharField(max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.timestamp) + ' ' + self.user.username

