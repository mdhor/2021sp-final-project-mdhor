from django.test import TestCase as DJTest
from django.urls import reverse


class TestUrls(DJTest):
    def test_line_chart(self):
        print(reverse("prisjakt:test_line_chart"))
        self.assertEqual(reverse("prisjakt:test_line_chart"), "/prisjakt/line_chart")

    def test_scatter_plot(self):
        print(reverse("prisjakt:test_scatter_plot"))
        self.assertEqual(
            reverse("prisjakt:test_scatter_plot"), "/prisjakt/scatter_plot"
        )
