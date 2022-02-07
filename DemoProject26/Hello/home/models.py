from django.db import models


# Create your models here.
class Stock(models.Model):
    stockName = models.CharField(max_length=100)
    qty = models.IntegerField()
    
    def __str__(self):
        return self.name
    