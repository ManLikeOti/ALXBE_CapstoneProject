from django.urls import path
from . import views

urlpatterns = [
    path('prescriptions/', views.PrescriptionListCreate.as_view(), name='prescription-list'),
    path('prescriptions/<int:pk>/', views.PrescriptionRetrieveUpdateDestroy.as_view(), name='prescription-detail'),
]