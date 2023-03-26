from django.test import TestCase
from django.utils import timezone

from .models import Playlist, PublishStateOptions
from videos.models import Video


class PlaylistModelTestCase(TestCase):
    def create_show_with_seasons(self):
        self.show = Playlist.objects.create(
            title='Game of thrones',            
        )
        self.season_1 = Playlist.objects.create(
            parent=self.show,
            title='season 1'
        )
        self.season_2 = Playlist.objects.create(
            parent=self.show,
            title='season 2'
        )
        self.season_3 = Playlist.objects.create(
            parent=self.show,
            title='season 3'
        )

    def create_videos(self):
        self.video_a = Video.objects.create(
            title='Title',
            video_id='qwe'
        )
        self.video_b = Video.objects.create(
            title='Title',
            video_id='qwer'
        )
        self.video_c = Video.objects.create(
            title='Title',
            video_id='qwert'
        )

    def setUp(self):
        self.create_videos()
        self.create_show_with_seasons()
        self.obj_a = Playlist.objects.create(
            title='This is my title',
            video=self.video_a,
            )
        self.obj_a.videos.set([self.video_a, self.video_b, self.video_c])
        self.obj_a.save()
        self.obj_b = Playlist.objects.create(
            title='This is my title',
            state=PublishStateOptions.PUBLISH,
            video=self.video_a
        )

    def test_show_with_seasons(self):
        shows = Playlist.objects.filter(parent__isnull=True)
        seasons = Playlist.objects.filter(parent__isnull=False)
        self.assertEqual(shows.count(), 3)
        self.assertEqual(seasons.count(), 3)

    def test_playlist_video_items(self):
        qs = self.obj_a.videos.all()
        self.assertEqual(qs.count(), 3)

    def test_video_playlist(self):
        qs = self.video_a.playlist_featured.all()
        self.assertEqual(qs.count(), 2)

    def test_video_playlist_ids_property(self):
        ids = self.obj_a.video.get_playlist_ids()
        # filtering m2m field with only one object
        Playlist.objects.filter(videos__in=[self.video_a])
        actual_ids = list(Playlist.objects.filter(video=self.video_a)
            .values_list('id', flat=True))
        self.assertEqual(ids, actual_ids)
            

    def test_valid_title(self):
        title = 'This is my title'
        qs = Playlist.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_account_created(self):
        qs = Playlist.objects.all()
        self.assertEqual(qs.count(), 6)

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