from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    year = models.IntegerField()
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) # forein key linking to a user account
    

    def __str__(self):
        macchina = f"A {self.color} {self.name} ({self.year})"
        return macchina



    def get_absolute_url(self):
        return reverse("car-detail", kwargs={"car_id": self.id}) 


    
