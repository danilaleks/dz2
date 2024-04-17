from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_main = models.BooleanField(default=False)    
    is_top = models.BooleanField(default=False)   

    def __str__(self):
        return self.name
