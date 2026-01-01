from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Shishir(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField(
        validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)]
    )
    email = models.EmailField(null=True, blank=True)
