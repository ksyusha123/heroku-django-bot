from app.internal.models.user import User


def add_user(telegram_username, telegram_id, password):
    return User.objects.create_user(telegram_username, telegram_id, password)


def set_phone(telegram_id, phone_number):
    user = User.objects.get(telegram_id=telegram_id)
    user.phone_number = phone_number
    user.save()


def get_user_data(telegram_username):
    return User.objects.get(telegram_username=telegram_username)
