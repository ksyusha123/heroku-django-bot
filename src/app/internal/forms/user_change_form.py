from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from app.internal.models.user import User


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ("telegram_username", "telegram_id", "phone_number", "password", "is_active", "is_staff")

    def clean_password(self):
        return self.initial["password"]
