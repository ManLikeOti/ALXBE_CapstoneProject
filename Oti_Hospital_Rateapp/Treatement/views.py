from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Prescription
from .serializers import PrescriptionSerializer

class PrescriptionListCreate(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class PrescriptionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer