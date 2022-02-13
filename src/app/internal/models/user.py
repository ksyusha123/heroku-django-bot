from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

from app.internal.models import user_manager


class User(AbstractBaseUser, PermissionsMixin):
    telegram_username = models.CharField(db_index=True, max_length=255, unique=True)
    telegram_id = models.CharField(db_index=True, max_length=255, unique=True)
    phone_regex = RegexValidator(
        regex=r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", code="Incorrect phone number"
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "telegram_username"
    REQUIRED_FIELDS = ["telegram_id"]

    objects = user_manager.UserManager()

    def __str__(self):
        return (
            f"username: {self.telegram_username}\n"
            f"telegram_id: {self.telegram_id}\n"
            f"phone number: {self.phone_number}\n"
            f"staff status: {self.is_staff}"
        )

    def to_dict(self):
        return {
            "telegram_username": self.telegram_username,
            "telegram_id": self.telegram_id,
            "phone_number": self.phone_number,
            "staff_status": self.is_staff,
        }
