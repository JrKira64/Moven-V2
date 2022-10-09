from django.db import models

# Create your models here.

class Roadtrip(models.Model):
    From = models.CharField(max_length=200)
    to = models.CharField(max_length=200)
    Date= models.DateField(blank=True, null=True)