from django.test import TestCase
from django.utils import timezone

from .models import Playlist, PublishStateOptions
from videos.models import Video


class PlaylistModelTestCase(TestCase):
    def setUp(self):
        self.video_a = Video.objects.create(
            title='Title',
            video_id='qwe'
        )
        self.obj_a = Playlist.objects.create(
            title='This is my title',
            video=self.video_a,
            # videos=
            )
        self.obj_b = Playlist.objects.create(
            title='This is my title',
            state=PublishStateOptions.PUBLISH,
            video=self.video_a
        )

    def test_video_playlist(self):
        qs = self.video_a.playlist_featured.all()
        self.assertEqual(qs.count(), 2)

    # def test_video_playlist_ids_property(self):
    #     ids = self.obj_a.video.get_playlist_ids()
    #     actual_ids = Playlist

    def test_valid_title(self):
        title = 'This is my title'
        qs = Playlist.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_account_created(self):
        qs = Playlist.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_draft_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertTrue(qs.count(), 1)

    def test_publish_case(self):
        timestamp = timezone.now()
        published_qs = Playlist.objects.filter(
            state=PublishStateOptions.PUBLISH,
            publish_timestamp__lte=timestamp
        )
        self.assertTrue(published_qs.exists())

    def test_slug_field(self):
        self.assertEqual(self.obj_a.slug, 'this-is-my-title')

    def test_publish_manager(self):
        published_qs = Playlist.objects.all().published()
        # calling 'published' method directly thanks to 'published' method in
        # PlaylistManager class 
        published_qs2 = Playlist.objects.published()
        self.assertTrue(published_qs.exists())
        self.assertTrue(published_qs2.exists())