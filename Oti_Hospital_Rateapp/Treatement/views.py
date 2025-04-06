from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User


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




class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user = User.objects.get(username=request.data['username'])
            serializer = UserSerializer(user)
            response.data['user'] = serializer.data
        return response