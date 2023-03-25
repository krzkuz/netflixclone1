from django.test import TestCase
from django.utils import timezone

from .models import Video, PublishStateOptions


class VideoModelTestCase(TestCase):
    def setUp(self):
        Video.objects.create(
            title='This is my title',
            video_id='asd'
            )
        Video.objects.create(
            title='This is my title',
            state=PublishStateOptions.PUBLISH,
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
        qs = Video.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertTrue(qs.count(), 1)

    def test_publish_case(self):
        timestamp = timezone.now()
        published_qs = Video.objects.filter(
            state=PublishStateOptions.PUBLISH,
            publish_timestamp__lte=timestamp
        )
        self.assertTrue(published_qs.exists())

    def test_slug_field(self):
        obj = Video.objects.get(video_id='asd')
        self.assertEqual(obj.slug, 'this-is-my-title')

    def test_publish_manager(self):
        published_qs = Video.objects.all().published()
        # calling 'published' method directly thanks to 'published' method in
        # VideoManager class 
        published_qs2 = Video.objects.published()
        self.assertTrue(published_qs.exists())
        self.assertTrue(published_qs2.exists())