from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import VideoUploadForm
from .models import Video


def home(request):
    return redirect('videos:upload')


@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploaded_by = request.user
            video.save()
            form.save_m2m()
            return redirect('videos:detail', pk=video.pk)
    else:
        form = VideoUploadForm()

    return render(request, 'videos/upload.html', {'form': form})


@login_required
def video_detail(request, pk):
    video = get_object_or_404(
        Video.objects.prefetch_related('tags'),
        pk=pk,
        uploaded_by=request.user,
    )
    return render(request, 'videos/detail.html', {'video': video})
