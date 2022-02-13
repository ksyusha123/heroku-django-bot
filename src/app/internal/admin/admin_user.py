from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from app.internal.forms.user_change_form import UserChangeForm
from app.internal.forms.user_creation_form import UserCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("telegram_username", "telegram_id", "phone_number", "is_staff")
    list_filter = ("is_staff",)
    fieldsets = (
        (None, {"fields": ("telegram_username", "password")}),
        ("Personal info", {"fields": ("telegram_id", "phone_number")}),
        ("Permissions", {"fields": ("is_staff",)}),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("telegram_username", "telegram_id", "password1", "password2")}),
    )
    search_fields = ("telegram_username",)
    ordering = ("telegram_username",)
    filter_horizontal = ()
