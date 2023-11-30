from typing import Any
from django.core.management.base import BaseCommand
from argparse import ArgumentParser
import subprocess

class Command(BaseCommand):
    help = 'git add .; git commit -m "str"; git push origin mater'
    
    def add_arguments(self, parser):
        parser.add_argument('--commit', type=str, help='Сообщение коммита')

    def handle(self, *args: Any, **options: Any) -> str | None:
        str_commit = options['commit']
        cmd1 = 'git add .'
        cmd2 = f'git commit -m "{str_commit}"'
        cmd3 = 'git push origin master'
        r_cmd1 = subprocess.check_output(cmd1)
        r_cmd2 = subprocess.check_output(cmd2)
        r_cmd3 = subprocess.check_output(cmd3)
        print(r_cmd1.decode('utf-8'))
        print(r_cmd2.decode('utf-8'))
        print(r_cmd3.decode('utf-8'))
