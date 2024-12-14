from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
import logging

logger = logging.getLogger(__name__)

class RegisterOrLoginView(APIView):
    def post(self, request):
        logger.debug("Получен запрос: %s", request.data)
        username = request.data.get('username')
        password = request.data.get('password', 'defaultpassword')
        logger.debug("Имя пользователя: %s, Пароль: %s", username, password)

        if not username:
            return Response({'error': 'Username is required.'}, status=status.HTTP_400_BAD_REQUEST)

        user, created = User.objects.get_or_create(username=username)

        if created:
            user.set_password(password)
            user.save()

        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        return Response({
            'refresh': str(refresh),
            'access': str(access),
            'message': 'User created.' if created else 'User exists. Tokens issued.'
        }, status=status.HTTP_200_OK)