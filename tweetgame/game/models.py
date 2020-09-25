from django.db import models

class TweetStats(models.Model):
    count   = models.IntegerField()
    correct = models.IntegerField(null=True) 
