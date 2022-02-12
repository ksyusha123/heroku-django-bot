from django.core.management.base import BaseCommand

from app.internal.bot import Bot


class Command(BaseCommand):
    def handle(self, *args, **options):
        Bot().run()
