from django.db import migrations


INITIAL_TAG_NAMES = ['拉球', '比赛', '多球练习']


def seed_tags(apps, schema_editor):
    tag_model = apps.get_model('videos', 'Tag')
    for name in INITIAL_TAG_NAMES:
        tag_model.objects.get_or_create(name=name)


def remove_seeded_tags(apps, schema_editor):
    tag_model = apps.get_model('videos', 'Tag')
    tag_model.objects.filter(name__in=INITIAL_TAG_NAMES).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_tags, remove_seeded_tags),
    ]
