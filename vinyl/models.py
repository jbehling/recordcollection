from django.db import models


class Recording(models.Model):
    title = models.CharField(max_length=1000)
    released = models.IntegerField()
    label = models.CharField(max_length=500)
    catalog_number = models.CharField(max_length=100)
# Create your models here.
