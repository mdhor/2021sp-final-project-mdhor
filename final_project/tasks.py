import os
from contextlib import contextmanager
from datetime import datetime, timedelta

import pandas as pd
from csci_utils.luigi.target import SuffixPreservingLocalTarget
from csci_utils.luigi.task import Requirement, Requires, TargetOutput
from luigi import IntParameter, ListParameter, Task
from luigi.contrib.external_program import ExternalProgramTask
from luigi.util import inherits
from pj_scraper.scraper import Scraper

from final_project.django_target import DjangoModelTarget
from prisjakt.models import Prices, Products


class ScrapeProducts(Task):

    categories = ListParameter(default=["mobiltelefoner", "smartklokker"])
    no_pages = IntParameter(default=1)

    now = datetime.now() + timedelta(days=1)
    output = TargetOutput(
        "./data/",
        file_pattern="day"
        + str(now.timetuple().tm_yday)
        + "-{task.__class__.__name__}-{salt}{self.ext}",
        target_class=SuffixPreservingLocalTarget,
        salted=True,
        ext=".parquet",
    )

    def run(self):
        s = Scraper()
        all_products = pd.DataFrame()

        for category in self.categories:
            temp_df = s.get_all_products_from_category(category, no_pages=self.no_pages)
            all_products = all_products.append(temp_df)

        with self.output().temporary_path() as fp:
            all_products.to_parquet(fp, compression="gzip")


@inherits(ScrapeProducts)
class ScrapePrices(Task):

    products = Requirement(ScrapeProducts)
    requires = Requires()

    now = datetime.now() + timedelta(days=1)
    output = TargetOutput(
        "./data/",
        file_pattern="day"
        + str(now.timetuple().tm_yday)
        + "-{task.__class__.__name__}-{salt}{self.ext}",
        target_class=SuffixPreservingLocalTarget,
        salted=True,
        ext=".parquet",
    )

    def run(self):
        s = Scraper()
        products = pd.read_parquet(
            self.products.output().path, columns=["product_number"]
        )
        products = products.astype(str)
        prices_and_retailers = s.get_sellers_and_prices_of_product_list(
            products.product_number
        )
        prices_and_retailers["timestamp"] = self.now
        with self.output().temporary_path() as fp:
            prices_and_retailers.to_parquet(fp, compression="gzip")


@inherits(ScrapePrices)
class LoadPricesToDatabase(ExternalProgramTask):

    prices = Requirement(ScrapePrices)
    requires = Requires()

    def program_args(self):
        return f"python manage.py load_prices --input_path {self.prices.output().path}".split(
            " "
        )

    def run(self):
        super().run()

    def output(self):
        ids = pd.read_parquet(
            self.prices.output().path,
            columns=["product_number", "seller_id", "timestamp"],
        )
        ids = [
            str(entry.product_number)
            + str(entry.seller_id)
            + str(entry.timestamp.timetuple().tm_yday)
            for entry in ids.itertuples()
        ]
        return DjangoModelTarget(Prices, unique_identifier=list(set(ids)))


@inherits(ScrapeProducts)
class LoadProductsToDatabase(ExternalProgramTask):

    products = Requirement(ScrapeProducts)
    requires = Requires()

    def program_args(self):
        return f"python manage.py load_products --input_path {self.products.output().path}".split(
            " "
        )

    def run(self):
        super().run()

    def output(self):
        ids = pd.read_parquet(self.products.output().path, columns=["product_number"])
        ids = ids.product_number.values
        return DjangoModelTarget(Products, product_number=list(set(ids)))


@contextmanager
def change_dir(relative_dir):
    """ Context manager for temporarily entering another dir """
    cwd = os.getcwd()
    try:
        os.chdir("./" + relative_dir)
        yield
    finally:
        if os.getcwd() is not cwd:
            os.chdir(cwd)
