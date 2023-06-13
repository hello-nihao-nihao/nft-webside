# myapp/management/commands/create_default_admin.py

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from store.models import Profile


class Command(BaseCommand):
    help = 'Create default admin if not exists'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Admin username')
        parser.add_argument('--password', type=str, help='Admin password')

    def handle(self, *args, **options):
        User = get_user_model()
        username = options['username'] or 'admin'
        password = options['password'] or 'password'
        if not User.objects.filter(username=username).exists():
            user=User.objects.create_superuser(username, password=password)

            if not Profile.objects.filter(user=user).exists():
                user_profile = Profile.objects.create(user=user)
                user_profile.bio = '我是管理员'
                user_profile.location = '广东'
                user_profile.profileimg = 'blank-profile-picture.png'
                user_profile.save()



            self.stdout.write(self.style.SUCCESS('Default admin created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Default admin already exists'))
