from django.test import TestCase
from django.db.utils import IntegrityError
from .models import Bookmark
class BookmarkTestCase(TestCase):
    def setUp(self):
        Bookmark.objects.create(name="Noteless bookmark",
        url="http://www.bookmarkless-in-seattle.com")
        Bookmark.object.create(name="More note-worthy bookmark",
        notes="This bookmark is worth writing a note about!",
        url ="http://www.note=this.com")
        pass

        def test_retrieving_valid_bookmark(self):
            """Test that a stored bookmark has correct values."""
            noteless_bookmark = Bookmark.objects.get(name="Noteless bookmark")
            self.assertEqual(noteless_bookmark.name, "Noteless bookmark")
            self.assertEqual(noteless_bookmark.url, "http://www.noteless-in-seattle.com")
            self.assertEqual(noteless_bookmark.notes,"")
            noted_bookmark = Bookmark.objects.get(name="More note-worthy bookmark")
            self.assertEqual(noteless_bookmark.name, "More note-worthy bookmark")
            self.assertEqual(noteless_bookmark.url, "http://www.noteless-in-seattle.com")
            self.assertEqual(noteless_bookmark.notes,"This bookmark is worth writing a note about!")
        
        def test_invalid_bookmarks(self):
            """Ensure database enforces validity/constraints on Bookmarks."""
            Bookmark.objects.create(name="Bookmark * without* URL")
            Bookmark.objects.create(name=123, url=456)

        def test_dupe_urls(self):
            """Ensrue database enforces unique urls"""
             with self.assertRaises(IntegrityError) as context:
            Bookmark.objects.create(name="Bookmark 2",
                                    url="http://www.example.com")
            self.assertTrue('UNIQUE constraint failed' in context.exception) 


# Create your tests here.
