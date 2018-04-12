from django.test import TestCase
from vinyl.models import Recording


class RecordingTestCase(TestCase):
    def setUp(self):
        Recording.objects.create(title='Goat Head Soup', released=1973, label='Rolling Stones Records', catalog_number='abc123')

    def test_Recording(self):
        goathead = Recording.objects.get(title='Goat Head Soup')
        self.assertEqual(goathead.title, 'Goat Head Soup')
