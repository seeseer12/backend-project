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



    def __str__(self):     
        # dunder method to return string representation of the object   
        return f"{self.name} ({self.email})"
    


class Car(models.Model):
    car_name= models.CharField(max_length=100)
    car_model= models.CharField(max_length=100)
    car_price= models.FloatField()
    car_speed= models.FloatField(default=50.0)

    def __str__(self):
        return f"{self.car_name} - {self.car_model}"
    
    @property
    def speed(self):
      if self.car_speed > 100:
        return "Fast"
      elif self.car_speed > 50:
        return "Medium"
      else:
        return "Slow"
