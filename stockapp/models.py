from re import T
from django.db import models

# Create your models here.

class StockList(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50 , null=False , unique=True)
    description = models.CharField(max_length=500 , null=True)
    videourl =models.CharField(max_length=500 , null=True)
    industry = models.CharField(max_length=30 , null=True)
    mcap = models.IntegerField(null=True , blank=True)

    def __str__(self):
        return self.name

