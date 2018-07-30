from django.db import models
import datetime

# Create your models here.
class Entry(models.Model):
    reason_1: models.CharField(max_length=100)
    reason_2: models.CharField(max_length=100)
    reason_3: models.CharField(max_length=100)
    goal: models.TextField(null=True, blank=True)
    date: models.DateField(("Date"), default=datetime.date.today)
    author: models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='entries')

    def __str__(self):
        return self.goal