from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    year = models.IntegerField()

    def __str__(self):
        macchina = f"{self.name} ({self.year}) - {self.color}"
        return macchina
