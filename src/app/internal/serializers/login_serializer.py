from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class LoginSerializer(serializers.Serializer):
    telegram_username = serializers.CharField(max_length=255)
    telegram_id = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        telegram_username = data.get("telegram_username", None)
        password = data.get("password", None)

        if not telegram_username:
            raise serializers.ValidationError("Telegram username is required to log in")

        if not password:
            raise serializers.ValidationError("A password is required to log in")

        user = authenticate(username=telegram_username, password=password)

        if not user:
            raise serializers.ValidationError("No users with this telegram username and password")

        if not user.is_active:
            raise serializers.ValidationError("This user has been deactivated")

        token, _ = Token.objects.get_or_create(user=user)

        return {"telegram_username": user.telegram_username, "telegram_id": user.telegram_id, "token": token.key}
