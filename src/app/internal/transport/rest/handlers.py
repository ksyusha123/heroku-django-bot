from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView

from app.internal.serializers import login_serializer, registration_serializer
from app.internal.services.user_service import set_phone


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = registration_serializer.RegistrationSerializer

    def post(self, request):
        user = request.data.get("user", {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = login_serializer.LoginSerializer

    def post(self, request):
        user = request.data.get("user", {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if not request.user.phone_number:
            raise ValidationError("No phone number")
        return Response(request.user.to_dict(), status=status.HTTP_200_OK)


class SetPhoneAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        phone_number = request.data.get("phone_number")
        set_phone(request.user.telegram_id, phone_number)
        resp = request.user.to_dict()
        resp["phone_number"] = phone_number
        return Response(resp, status=status.HTTP_200_OK)
