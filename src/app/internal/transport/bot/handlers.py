from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.utils import IntegrityError
from rest_framework.authtoken.models import Token
from telegram import Update
from telegram.ext import CallbackContext

from app.internal.services import user_service


def start(update: Update, context: CallbackContext):
    args = update.message.text.split()
    tg_id = update.effective_chat.id
    if len(args) == 1:
        context.bot.send_message(
            chat_id=tg_id, text="Create password and use this command again.\nExample: /start mysecret"
        )
        return
    password = args[1]
    try:
        user = user_service.add_user(update.effective_chat.username, tg_id, password)
    except IntegrityError:
        context.bot.send_message(chat_id=tg_id, text="You are already our user")
    else:
        context.bot.send_message(chat_id=tg_id, text="Saved information about you")
        token, _ = Token.objects.get_or_create(user=user)
        context.bot.send_message(chat_id=tg_id, text=f"Your authorization token:\n{token}")


def set_phone(update: Update, context: CallbackContext):
    args = update.message.text.split()
    tg_id = update.effective_chat.id
    if len(args) == 1:
        context.bot.send_message(
            chat_id=tg_id,
            text="Use this command with your phone number\nExample: /set_phone +99999999999",
        )
        return
    phone_number = args[1]
    try:
        user_service.set_phone(update.effective_chat.id, phone_number)
        message = "Saved your phone number to the database"
    except ObjectDoesNotExist:
        message = "I don't know you :(\nPlease use /start"
    except ValidationError:
        message = "Wrong phone number :("
    except:
        message = "Something went wrong :("
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def me(update: Update, context: CallbackContext):
    user = user_service.get_user_data(update.effective_chat.username)
    if not user:
        message = "I don't know you :(\n" "Please use /start and /set_phone"
    elif not user.phone_number:
        message = "I don't know your phone number :(\n" "Please use /set_phone"
    else:
        message = f"Information about you:\n{str(user)}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
