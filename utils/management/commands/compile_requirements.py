from django.core.management.base import BaseCommand
import subprocess
import os


class Command(BaseCommand):

    help = 'pip-compiles all requirements'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        FNULL = open(os.devnull, 'w')

        subprocess.call(["pip-compile", "requirements/development.in"], stdout=FNULL)
        subprocess.call(["pip-compile", "requirements/production.in"], stdout=FNULL)
        subprocess.call(["pip-compile", "requirements/test.in"], stdout=FNULL)