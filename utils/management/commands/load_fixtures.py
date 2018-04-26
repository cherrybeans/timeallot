import logging
import signal
import sys

from django.core.management import BaseCommand as DjangoBaseCommand
from django.core.management import call_command

log = logging.getLogger(__name__)


class BaseCommand(DjangoBaseCommand):
    """
    Base command for our management commands. Implement the .run() function.
    """

    def handle(self, *args, **options):
        """
        Set log level based on builtin -v or --verbose flag.
        -v 0 CRITICAL
        -v 1 INFO
        -v 2 DEBUG
        """
        self.verbosity = getattr(self, 'verbosity', options['verbosity'])
        log_levels = {
            0: logging.WARNING,
            1: logging.INFO,
            2: logging.DEBUG,
            3: logging.DEBUG
        }

        root_log = logging.getLogger('')
        for handler in root_log.handlers:
            handler.setLevel(log_levels[self.verbosity])

        try:
            # Gracefully exit on sigterm.
            signal.signal(signal.SIGTERM, self._handle_sigterm)

            # A SIGUSR1 signals an exit with an autorestart
            signal.signal(signal.SIGUSR1, self._handle_sigusr1)

            # Handle Keyboard Interrupt
            signal.signal(signal.SIGINT, self._handle_sigterm)

            return self.run(*args, **options)

        except Exception:
            log.exception('Fatal exception, exiting...')
            sys.exit(1)

    def _handle_sigterm(self, signum, frame):
        self.close()
        sys.exit(0)

    def _handle_sigusr1(self, signum, frame):
        self._handle_sigterm(signum, frame)

    def run(self, *args, **options):
        raise NotImplementedError('Please implement the .run method')

    def close(self):
        pass


class Command(BaseCommand):

    help = 'Loads initial data from fixtures. Running it again will ' \
           'override data if there has been changes.'

    def call_command(self, *args, **options):
        call_command(*args, verbosity=self.verbosity, **options)

    def load_fixtures(self, fixtures):
        for fixture in fixtures:
            path = 'timeallot/apps/{}'.format(fixture)
            self.call_command('loaddata', path)

    def run(self, *args, **options):
        log.info('Loading fixtures from all apps:')

        # Add more fixtures to load here. Order does matter due to dependencies.
        self.load_fixtures([
            'user/fixtures/users.yaml',
            'timer/fixtures/categories.yaml',
            'timer/fixtures/projects.yaml',
            'timer/fixtures/subtags.yaml',
            'timer/fixtures/sessions.yaml',
        ])

        log.info('Done!')
