import shutil
import tempfile

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Tag, Video


TEST_MEDIA_ROOT = tempfile.mkdtemp(prefix='tennis-video-hub-tests-')


@override_settings(MEDIA_ROOT=TEST_MEDIA_ROOT)
class VideoFlowTests(TestCase):
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEST_MEDIA_ROOT, ignore_errors=True)

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='owner',
            password='test-password',
        )

    @staticmethod
    def video_file(name='point.mp4'):
        return SimpleUploadedFile(
            name,
            b'fake-mp4-content',
            content_type='video/mp4',
        )

    def valid_payload(self):
        tag = Tag.objects.get(name='拉球')
        return {
            'file': self.video_file(),
            'player_count': 2,
            'camera_shaking': 'False',
            'viewpoint': Video.Viewpoint.TRIPOD,
            'tags': [tag.pk],
        }

    def test_seed_tags_are_available(self):
        self.assertEqual(
            set(Tag.objects.values_list('name', flat=True)),
            {'拉球', '比赛', '多球练习'},
        )

    @override_settings(DEBUG=True)
    def test_local_test_admin_command_creates_documented_superuser(self):
        call_command('create_test_admin', verbosity=0)

        test_admin = get_user_model().objects.get(username='testadmin')
        self.assertTrue(test_admin.is_staff)
        self.assertTrue(test_admin.is_superuser)
        self.assertTrue(test_admin.check_password('TennisTest-001!'))

    def test_upload_requires_login(self):
        response = self.client.get(reverse('videos:upload'))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('videos:upload')}",
        )

    def test_logged_in_user_can_upload_and_open_detail(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('videos:upload'), self.valid_payload())

        video = Video.objects.get()
        self.assertRedirects(response, reverse('videos:detail', args=[video.pk]))
        self.assertEqual(video.uploaded_by, self.user)
        self.assertEqual(video.player_count, 2)
        self.assertFalse(video.camera_shaking)
        self.assertEqual(video.viewpoint, Video.Viewpoint.TRIPOD)
        self.assertEqual(list(video.tags.values_list('name', flat=True)), ['拉球'])

        detail = self.client.get(reverse('videos:detail', args=[video.pk]))
        self.assertContains(detail, '<video', html=False)
        self.assertContains(detail, '支架视角')
        self.assertContains(detail, '拉球')

    def test_non_mp4_file_is_rejected_without_a_record(self):
        self.client.force_login(self.user)
        payload = self.valid_payload()
        payload['file'] = self.video_file('notes.txt')

        response = self.client.post(reverse('videos:upload'), payload)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '目前只支持 MP4 视频。')
        self.assertFalse(Video.objects.exists())

    @override_settings(MAX_VIDEO_UPLOAD_SIZE_BYTES=15)
    def test_oversized_file_is_rejected_without_a_record(self):
        self.client.force_login(self.user)
        payload = self.valid_payload()
        payload['file'] = self.video_file()

        response = self.client.post(reverse('videos:upload'), payload)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '视频文件不能超过 50 MB。')
        self.assertFalse(Video.objects.exists())

    def test_player_count_outside_one_to_four_is_rejected(self):
        self.client.force_login(self.user)
        payload = self.valid_payload()
        payload['player_count'] = 5

        response = self.client.post(reverse('videos:upload'), payload)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '确保该值小于或等于4。')
        self.assertFalse(Video.objects.exists())

    def test_user_cannot_open_another_users_video_detail(self):
        another_user = get_user_model().objects.create_user(
            username='another',
            password='test-password',
        )
        video = Video.objects.create(
            file=self.video_file(),
            player_count=1,
            camera_shaking=True,
            viewpoint=Video.Viewpoint.FLOOR,
            uploaded_by=another_user,
        )
        self.client.force_login(self.user)

        response = self.client.get(reverse('videos:detail', args=[video.pk]))

        self.assertEqual(response.status_code, 404)
