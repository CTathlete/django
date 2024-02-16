import django.shortcuts as ds
from django.test import SimpleTestCase

class MakeToastTests(SimpleTestCase):
    def test_make_toast(self):
        self.assertEqual(ds.make_toast(), "toast")