from django.core.management import call_command
from django.test import TestCase as DJTest


class TestLoadPrice(DJTest):
    def test_raises_without_input(self):
        with self.assertRaises(RuntimeWarning):
            call_command("load_prices")
