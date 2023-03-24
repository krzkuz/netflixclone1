from django.test import TestCase
from django.utils import timezone

from .models import Video


class VideoModelTestCase(TestCase):
    def setUp(self):
        Video.objects.create(
            title='This is my title',
            video_id='asd'
            )
        Video.objects.create(
            title='This is my title',
            state=Video.VideoStateOptions.PUBLISH,
            video_id='qwe'
        )

    def test_valid_title(self):
        title = 'This is my title'
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_account_created(self):
        qs = Video.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_draft_case(self):
        qs = Video.objects.filter(state=Video.VideoStateOptions.DRAFT)
        self.assertTrue(qs.count(), 1)

    def test_publish_case(self):
        timestamp = timezone.now()
        published_qs = Video.objects.filter(
            state=Video.VideoStateOptions.PUBLISH,
            publish_timestamp__lte=timestamp
        )
        self.assertTrue(published_qs.exists())

    def test_slug_field(self):
        obj = Video.objects.get(video_id='asd')
        self.assertEqual(obj.slug, 'this-is-my-title')