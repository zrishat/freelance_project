from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
# from freelance_app.models import MyUser
from django.contrib.auth.models import Group, User, Permission

class Command(BaseCommand):
    help = 'Work with db'

    def handle(self, *args, **options):
        # Удаление
        User.objects.all().delete()
        Group.objects.all().delete()

        User.objects.create_superuser('admin', 'admin@local.domain', password='admin')

        # Создание групп
        groups = ['customer', 'executer', 'support']
        for group in groups:
            Group.objects.get_or_create(name=group)


        # Создание пользователей
        for number in range(1, 4):
            print(number)
            users = ['customer', 'executer', 'support']
            for user in users:
                username = user+str(number)
                User.objects.create_user(username=username,
                                           email=f'{username}@local.domain',
                                           password=f'{username}_123456')
                # Назначение групп пользователям
                u = User.objects.get(username=username)
                if 'customer' in user:
                    my_group = Group.objects.get(name='customer')
                if 'executer' in user:
                    my_group = Group.objects.get(name='executer')
                if 'support' in user:
                    my_group = Group.objects.get(name='support')
                my_group.user_set.add(u)

        print('done')
