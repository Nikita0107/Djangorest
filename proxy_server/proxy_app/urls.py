from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import RegisterOrLoginView
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "Добро пожаловать в API прокси сервера!"})

urlpatterns = [
    path('register/', RegisterOrLoginView.as_view(), name='register_or_login'),
    path('', api_home, name='api_home'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/register/', RegisterOrLoginView.as_view(), name='register_or_login'),
]