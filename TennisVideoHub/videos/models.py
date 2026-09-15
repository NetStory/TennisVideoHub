import uuid

from django.conf import settings
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.db import models

from .validators import validate_video_file_size


def video_upload_path(instance, filename):
    """Use generated names so user filenames cannot collide or shape paths."""
    return f'videos/{instance.uploaded_by_id}/{uuid.uuid4().hex}.mp4'


class Tag(models.Model):
    name = models.CharField('标签名称', max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Video(models.Model):
    class Viewpoint(models.TextChoices):
        FLOOR = 'floor', '地板视角'
        TRIPOD = 'tripod', '支架视角'
        HIGH = 'high', '高位摄像机视角'

    file = models.FileField(
        '视频文件',
        upload_to=video_upload_path,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['mp4'],
                message='目前只支持 MP4 视频。',
            ),
            validate_video_file_size,
        ],
    )
    player_count = models.PositiveSmallIntegerField(
        '场上人数',
        validators=[MinValueValidator(1), MaxValueValidator(4)],
    )
    camera_shaking = models.BooleanField('相机是否晃动')
    viewpoint = models.CharField(
        '拍摄视角',
        max_length=16,
        choices=Viewpoint.choices,
    )
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='uploaded_videos',
        verbose_name='上传用户',
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='videos',
        verbose_name='标签',
    )
    created_at = models.DateTimeField('上传时间', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = '网球视频'
        verbose_name_plural = '网球视频'

    def __str__(self):
        return f'视频 #{self.pk}' if self.pk else '新视频'
