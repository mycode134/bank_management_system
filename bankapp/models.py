from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    mobel=models.IntegerField(max_length=10)
    account_no=models.IntegerField(max_length=14)
    balance=models.FloatField(max_length=15)

    def __str__(self):
        return self.name