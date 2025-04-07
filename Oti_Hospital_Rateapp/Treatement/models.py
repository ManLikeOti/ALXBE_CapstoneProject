from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Prescription(models.Model):
    drug = models.CharField(max_length=200)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    prescription_date = models.DateField(default=datetime.date.today)
    dosage = models.IntegerField()

    def __str__(self):
        return self.drug