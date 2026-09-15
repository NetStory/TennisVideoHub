from django.conf import settings
from django.core.exceptions import ValidationError


MAX_VIDEO_FILE_SIZE_BYTES = 50 * 1024 * 1024


def validate_video_file_size(video_file):
    """Keep the first local upload slice bounded to non-empty files <= 50 MB."""
    size = getattr(video_file, 'size', None)
    size_limit = getattr(
        settings,
        'MAX_VIDEO_UPLOAD_SIZE_BYTES',
        MAX_VIDEO_FILE_SIZE_BYTES,
    )
    if size == 0:
        raise ValidationError('视频文件不能为空。')
    if size is not None and size > size_limit:
        raise ValidationError('视频文件不能超过 50 MB。')
