from django.db import models
from django.utils import timezone

class LongToShort(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

class ClickAnalytics(models.Model):
    url = models.ForeignKey(LongToShort, on_delete=models.CASCADE)
    device = models.CharField(max_length=50)
    country = models.CharField(max_length=100, default="India")  
    timestamp = models.DateTimeField(default=timezone.now)
