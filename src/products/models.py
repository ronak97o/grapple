from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)

    description = models.TextField()
    price = models.DecimalField(decimal_places =2,max_digits=20,default='10.00')

    def __str__(self):
        return self.title

class Order(models.Model):
    shopname = models.CharField(max_length=128)
    items = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    user = models.ForeignKey(User, null=True, blank=True)
    
    def __str__(self):
        return self.shopname