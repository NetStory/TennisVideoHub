import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import videos.models
import videos.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='标签名称')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'file',
                    models.FileField(
                        upload_to=videos.models.video_upload_path,
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=['mp4'],
                                message='目前只支持 MP4 视频。',
                            ),
                            videos.validators.validate_video_file_size,
                        ],
                        verbose_name='视频文件',
                    ),
                ),
                (
                    'player_count',
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(4),
                        ],
                        verbose_name='场上人数',
                    ),
                ),
                ('camera_shaking', models.BooleanField(verbose_name='相机是否晃动')),
                (
                    'viewpoint',
                    models.CharField(
                        choices=[
                            ('floor', '地板视角'),
                            ('tripod', '支架视角'),
                            ('high', '高位摄像机视角'),
                        ],
                        max_length=16,
                        verbose_name='拍摄视角',
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
                (
                    'tags',
                    models.ManyToManyField(blank=True, related_name='videos', to='videos.tag', verbose_name='标签'),
                ),
                (
                    'uploaded_by',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='uploaded_videos',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='上传用户',
                    ),
                ),
            ],
            options={
                'verbose_name': '网球视频',
                'verbose_name_plural': '网球视频',
                'ordering': ['-created_at'],
            },
        ),
    ]
