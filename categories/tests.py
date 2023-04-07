from django.test import TestCase

from .models import Category
from playlists.models import Playlist

class CategoryTestCase(TestCase):
    def setUp(self):
        self.cat_a = Category.objects.create(title='Action')
        self.cat_b = Category.objects.create(title='Comedy', active=False)
        self.play_a = Playlist.objects.create(
            title='My title',
            category=self.cat_a
        )

    def test_is_active(self):
        self.assertTrue(self.cat_a.active)

    def test_not_is_active(self):
        self.assertFalse(self.cat_b.active)

    def test_playlist_category(self):
        category = self.play_a.category
        self.assertEqual(category, self.cat_a)