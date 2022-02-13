from django.urls import path

from app.internal.transport.rest.handlers import LoginAPIView, RegistrationAPIView, UserAPIView

urlpatterns = [
    path("users/", RegistrationAPIView.as_view()),
    path("users/login/", LoginAPIView.as_view()),
    path("users/me/", UserAPIView.as_view()),
]
