from unittest import TestCase
from unittest.mock import MagicMock, patch

import pandas as pd
from pj_scraper.scraper import Scraper

from final_project.tasks import ScrapeProducts  # , ScrapePrices


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
    def test_integrated(self, mock_to_parquet):
        assert False


class TestLoadProductsToDatabase(TestCase):
    def test_integrated(self):
        assert False


class TestLoadPricesToDatabase(TestCase):
    def test_integrated(self):
        assert False


class MiscTests(TestCase):
    def test_chg_dir_contextmanager(self):
        assert False
