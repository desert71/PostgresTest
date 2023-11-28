from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Zen of Python'

    def handle(self, *args: Any, **options: Any) -> str | None:
        import this