import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from prisjakt.models import Prices, Products


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--input_path")

    def handle(self, *args, **options):

        if not options["input_path"]:
            raise RuntimeWarning("No input path provided")

        prices = pd.read_parquet(options["input_path"])
        entries = [
            Prices(
                price_id=entry.price_id,
                seller_product_name=entry.seller_product_name,
                stock_status=entry.stock_status,
                price_incl_shipping=entry.price_incl_shipping,
                price_excl_shipping=entry.price_excl_shipping,
                seller_id=entry.seller_id,
                seller_name=entry.seller_name,
                seller_rating=entry.seller_rating,
                product_number=Products.objects.get(
                    product_number=entry.product_number
                ),
                timestamp=entry.timestamp,
                unique_identifier=str(entry.product_number)
                + str(entry.seller_id)
                + str(entry.timestamp.timetuple().tm_yday),
            )
            for entry in prices.itertuples()
        ]
        with transaction.atomic():
            Prices.objects.bulk_create(entries, ignore_conflicts=True)
