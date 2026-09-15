from django import forms

from .models import Video


class VideoUploadForm(forms.ModelForm):
    camera_shaking = forms.TypedChoiceField(
        label='相机是否晃动',
        choices=(('True', '是'), ('False', '否')),
        coerce=lambda value: value == 'True',
        widget=forms.RadioSelect,
        error_messages={'required': '请选择相机是否晃动。'},
    )

    class Meta:
        model = Video
        fields = ['file', 'player_count', 'camera_shaking', 'viewpoint', 'tags']
        widgets = {
            'file': forms.ClearableFileInput(
                attrs={'accept': '.mp4,video/mp4'},
            ),
            'player_count': forms.NumberInput(
                attrs={'min': 1, 'max': 4, 'inputmode': 'numeric'},
            ),
            'viewpoint': forms.RadioSelect,
            'tags': forms.CheckboxSelectMultiple,
        }
        help_texts = {
            'file': '目前只接受不超过 50 MB 的 MP4 文件。',
            'player_count': '填写视频画面中实际参与击球的人数（1-4）。',
            'tags': '可以多选，也可以暂时不选。',
        }
        error_messages = {
            'file': {'required': '请选择一个 MP4 视频。'},
            'player_count': {'required': '请填写场上人数。'},
            'viewpoint': {'required': '请选择拍摄视角。'},
        }
