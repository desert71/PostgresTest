from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Команда для вывода приветствия в консоль'
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write('Приветствую, пользователь!')