import pandas as pd
from django.core.management.base import BaseCommand
from prisjakt.models import Products


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--input_path")

    def handle(self, *args, **options):

        if not options["input_path"]:
            raise RuntimeWarning("No input path provided")

        products = pd.read_parquet(options["input_path"])
        entries = [
            Products(
                product_number=entry.product_number,
                product_name=entry.product_name,
                category=entry.category,
            )
            for entry in products.itertuples()
        ]
        Products.objects.bulk_create(entries, ignore_conflicts=True)

        from django_pandas.io import read_frame

        qs = Products.objects.all()
        df = read_frame(qs)
        df.to_csv("../data/prods_from_db.csv")
        print(df)
