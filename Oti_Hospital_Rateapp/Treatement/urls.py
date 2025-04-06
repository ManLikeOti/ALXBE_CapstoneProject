from django.urls import path
from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView,
    CustomTokenObtainPairView,
    UserDetailView,
)


urlpatterns = [
    path('prescriptions/', views.PrescriptionListCreate.as_view(), name='prescription-list'),
    path('prescriptions/<int:pk>/', views.PrescriptionRetrieveUpdateDestroy.as_view(), name='prescription-detail'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', UserDetailView.as_view(), name='user_detail'),
]