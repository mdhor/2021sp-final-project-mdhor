import datetime
from unittest.mock import patch

import pandas as pd
from django.core.management import call_command
from django.test import TestCase as DJTest

from prisjakt.models import Prices, Products


class TestLoadPrice(DJTest):
    def test_raises_without_input(self):
        with self.assertRaises(RuntimeWarning):
            call_command("load_prices")

    def test_load_products(self):
        with patch("pandas.read_parquet") as mock_read_parquet:
            mock_read_parquet.return_value = pd.DataFrame(
                {
                    "product_number": [1, 2],
                    "product_name": ["1", "2"],
                    "category": ["c1", "c2"],
                }
            )
            call_command("load_products", input_path="foo")
            self.assertEqual(Products.objects.get(product_number=1).product_name, "1")
            self.assertEqual(Products.objects.get(product_number=2).product_name, "2")

    def test_load_prices(self):
        with patch("pandas.read_parquet") as mock_read_parquet:
            mock_read_parquet.return_value = pd.DataFrame(
                {
                    "product_number": [1, 2],
                    "product_name": ["1", "2"],
                    "category": ["c1", "c2"],
                }
            )
            call_command("load_products", input_path="foo")
        with patch("pandas.read_parquet") as mock_read_parquet:
            mock_read_parquet.return_value = pd.DataFrame(
                {
                    "price_id": [1, 2],
                    "seller_product_name": ["sp1", "sp2"],
                    "stock_status": ["stock1", "stock2"],
                    "price_incl_shipping": [1.0, 2.0],
                    "price_excl_shipping": [1.0, 2.0],
                    "seller_id": [1, 2],
                    "seller_name": ["s1", "s2"],
                    "seller_rating": [1.0, 2.0],
                    "product_number": [1, 2],
                    "timestamp": [datetime.datetime.now(), datetime.datetime.now()],
                }
            )
            call_command("load_prices", input_path="foo")
            self.assertEqual(
                Prices.objects.get(price_id=1).unique_identifier,
                "11" + str(datetime.datetime.now().timetuple().tm_yday),
            )
            self.assertEqual(
                Prices.objects.get(price_id=2).unique_identifier,
                "22" + str(datetime.datetime.now().timetuple().tm_yday),
            )
