from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings

class Command(BaseCommand):
    help = 'Creates an admin user if it doesn\'t exist'

    def add_arguments(self, parser):
        parser.add_argument('--username', default='admin', help='Admin username')
        parser.add_argument('--email', default='admin@example.com', help='Admin email')
        parser.add_argument('--password', default='adminpassword', help='Admin password')

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'Admin user "{username}" already exists'))
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f'Admin user "{username}" created successfully'))
        self.stdout.write(self.style.SUCCESS(f'You can now log in at /admin/ with username: {username} and the password you provided')) 