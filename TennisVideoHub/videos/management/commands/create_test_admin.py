from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


TEST_ADMIN_USERNAME = 'testadmin'
TEST_ADMIN_PASSWORD = 'TennisTest-001!'


class Command(BaseCommand):
    help = 'Create or reset the documented local-only test administrator.'

    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise CommandError('测试管理员只能在 DEBUG=True 的本地环境中创建。')

        user_model = get_user_model()
        user, created = user_model.objects.get_or_create(username=TEST_ADMIN_USERNAME)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(TEST_ADMIN_PASSWORD)
        user.save()

        action = '已创建' if created else '已重置'
        self.stdout.write(
            self.style.SUCCESS(f'{action}本地测试管理员：{TEST_ADMIN_USERNAME}')
        )
