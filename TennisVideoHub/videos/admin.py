from django.contrib import admin

from .models import Tag, Video


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'uploaded_by', 'player_count', 'viewpoint', 'created_at']
    list_filter = ['camera_shaking', 'viewpoint', 'tags']
    search_fields = ['uploaded_by__username']
    filter_horizontal = ['tags']
