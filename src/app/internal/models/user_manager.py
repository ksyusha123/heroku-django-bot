from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, telegram_username, telegram_id, password=None):
        if not telegram_username:
            raise TypeError("Users must have telegram username")
        if not telegram_id:
            raise TypeError("Users must have telegram id")

        user = self.model(telegram_username=telegram_username, telegram_id=telegram_id)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, telegram_username, telegram_id, password):
        if password is None:
            raise TypeError("Superusers must have a password")

        user = self.create_user(telegram_username, telegram_id, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
