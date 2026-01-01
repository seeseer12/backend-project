from django.db import models

# Create your models here.
class Shishir(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    city=models.CharField(max_length=100)
    phone=models.PositiveBigIntegerField(max_length=10)