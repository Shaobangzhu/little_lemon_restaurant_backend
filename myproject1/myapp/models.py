from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    reservation_day = models.CharField(max_length=20)
    seats = models.IntegerField()
    
    def __str__(self):
        return self.name