from django.test import TestCase as DJTest

from prisjakt.models import Prices, Products


class TestModels(DJTest):
    def test_products_fields(self):
        model = Products.objects.create(
            product_number=1,
            product_name="1",
            category="c",
        )
        field_names = [field.name for field in model._meta.fields]
        map(
            lambda field: self.assertTrue(field in field_names),
            ["product_number", "product_name", "category"],
        )

    def test_products_field_data(self):
        model = Products.objects.create(
            product_number=1,
            product_name="1",
            category="c",
        )
        self.assertEqual(model.product_number, 1)
        self.assertEqual(model.product_name, "1")
        self.assertEqual(model.category, "c")

    def test_factreview_fields(self):
        model = Products.objects.create(
            product_number=1,
            product_name="1",
            category="c",
        )
        prices = Prices.objects.create(
            price_id=1,
            seller_product_name="prod",
            stock_status="stock",
            price_incl_shipping=1.0,
            price_excl_shipping=2.0,
            seller_id=2,
            seller_name="seller",
            seller_rating=3.0,
            product_number=model,
        )
        field_names = [field.name for field in prices._meta.fields]
        map(
            lambda field: self.assertTrue(field in field_names),
            [
                "price_id",
                "seller_product_name",
                "stock_status",
                "timestamp",
                "unique_identifier",
            ],
        )

    def test_factreview_field_data(self):
        model = Products.objects.create(
            product_number=1,
            product_name="1",
            category="c",
        )
        prices = Prices.objects.create(
            price_id=1,
            seller_product_name="prod",
            stock_status="stock",
            price_incl_shipping=1.0,
            price_excl_shipping=2.0,
            seller_id=2,
            seller_name="seller",
            seller_rating=3.0,
            product_number=model,
        )
        self.assertEqual(prices.price_id, 1)
        self.assertEqual(prices.seller_rating, 3.0)
        self.assertEqual(prices.seller_name, "seller")
