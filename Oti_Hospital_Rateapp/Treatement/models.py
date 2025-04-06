from django.db import models

# Create your models here.

class Prescription(models.Model):
    drug = models.CharField(max_length=200)
    doctor = models.CharField(max_length=100)
    prescription_date = models.DateField()
    dosage = models.IntegerField()

    def __str__(self):
        return self.doctor