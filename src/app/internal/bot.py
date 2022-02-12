import inspect
import logging

from telegram.ext import CommandHandler, Updater

from app.internal.transport.bot import handlers
from config.settings import BOT_TOKEN


class Bot:
    def __init__(self):
        self.updater = Updater(token=BOT_TOKEN)
        self.register_handlers()

    def run(self):
        logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
        self.updater.start_polling()
        self.updater.idle()

    def register_handlers(self):
        handlers_functions = inspect.getmembers(handlers, inspect.isfunction)
        dispatcher = self.updater.dispatcher
        for handler_function in handlers_functions:
            current_handler = CommandHandler(handler_function[0], handler_function[1])
            dispatcher.add_handler(current_handler)
