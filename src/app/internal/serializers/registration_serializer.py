from rest_framework import serializers

from app.internal.models import user
from app.internal.services.user_service import add_user


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = user.User
        fields = ["telegram_username", "telegram_id", "phone_number", "password", "token"]

    def create(self, validated_data):
        return add_user(**validated_data)
