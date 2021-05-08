import os
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import MagicMock, patch

import pandas as pd
from pj_scraper.scraper import Scraper

from final_project.tasks import ScrapePrices, ScrapeProducts, change_dir


class TestScrapeProducts(TestCase):
    @patch("pandas.DataFrame.to_parquet")
    def test_integrated(self, mock_to_parquet):
        Scraper.get_all_products_from_category = MagicMock()
        Scraper.get_all_products_from_category.return_value = pd.DataFrame(
            {"col1": [1]}
        )

        task = ScrapeProducts()
        task.run()

        Scraper.get_all_products_from_category.assert_called()
        mock_to_parquet.assert_called()


class TestScrapePrices(TestCase):
    @patch("pandas.DataFrame.to_parquet")
    @patch("pandas.read_parquet")
    def test_integrated(self, mock_from_parquet, mock_to_parquet):
        Scraper.get_sellers_and_prices_of_product_list = MagicMock()
        Scraper.get_sellers_and_prices_of_product_list.return_value = pd.DataFrame(
            {"col1": [1]}
        )

        mock_from_parquet.return_value = pd.DataFrame({"product_number": [1]})

        task = ScrapePrices()
        task.run()

        Scraper.get_sellers_and_prices_of_product_list.assert_called()
        mock_to_parquet.assert_called()


class MiscTests(TestCase):
    def test_chg_dir_contextmanager(self):
        original_d = os.getcwd()
        with TemporaryDirectory(dir="./") as td:
            full_td = original_d + "/" + td.split("/")[-1]
            with change_dir(td.split("/")[-1]):
                self.assertEqual(os.getcwd(), full_td)
            self.assertEqual(os.getcwd(), original_d)
