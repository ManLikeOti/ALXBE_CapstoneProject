from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Prescription(models.Model):
    drug = models.CharField(max_length=200)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    prescription_date = models.DateField()
    dosage = models.IntegerField()

    def __str__(self):
        return self.drug