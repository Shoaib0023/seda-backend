from django.core.management import BaseCommand

from signals.apps.signals.models import Category


class Command(BaseCommand):
    help = 'Custom Commands'

    def handle(self, *args, **options):
        self.stdout.write('Working')
