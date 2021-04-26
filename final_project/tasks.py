from datetime import datetime

import pandas as pd
from csci_utils.luigi.target import SuffixPreservingLocalTarget
from csci_utils.luigi.task import Requirement, Requires, TargetOutput
from luigi import IntParameter, ListParameter, Task
from luigi.util import inherits
from pj_scraper.scraper import Scraper


class ScrapeProducts(Task):

    categories = ListParameter(default=["mobiltelefoner", "smartklokker"])
    no_pages = IntParameter(default=1)

    output = TargetOutput(
        "./data/",
        file_pattern="day"
        + str(datetime.now().timetuple().tm_yday)
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

    now = datetime.now()
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
        prices_and_retailers = s.get_sellers_and_prices_of_product_list(
            pd.read_parquet(self.products.output().path)["product_number"]
        )
        prices_and_retailers["timestamp"] = self.now
        with self.output().temporary_path() as fp:
            prices_and_retailers.to_parquet(fp, compression="gzip")
