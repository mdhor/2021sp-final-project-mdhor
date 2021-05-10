from django.test import TestCase as DJTest

from final_project.django_target import DjangoModelTarget
from prisjakt.models import Products


class TestDjangoTarget(DJTest):
    def setUp(self):
        Products.objects.create(product_number=1)
        Products.objects.create(product_number=2)

    def test_get(self):
        target = DjangoModelTarget(Products, product_number=[1, 2])
        out = target.get()
        self.assertEqual(out[0].product_number, 1)
        self.assertEqual(out[1].product_number, 2)

    def test_exists_true(self):
        target = DjangoModelTarget(Products, product_number=[1, 2])
        self.assertTrue(target.exists())

    def test_exists_false(self):
        target = DjangoModelTarget(Products, product_number=[1, 2, 3])
        self.assertFalse(target.exists())
