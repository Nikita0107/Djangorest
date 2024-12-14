from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Создаём пользователя с хэшированием пароля
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),  # email может быть пустым
            password=validated_data['password']
        )
        return user