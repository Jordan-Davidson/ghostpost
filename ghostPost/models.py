from django.db import models
from django.utils import timezone

# Create your models here.

class RoastBoast(models.Model):
    roastBoast = models.BooleanField()
    post = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)
    def __str__(self):
        if self.roastBoast == True:
            return 'Roast'
        else:
            return 'Boast'