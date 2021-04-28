import pandas as pd
from chartjs.views.lines import BaseLineChartView
from django.db.models.functions import TruncDate
from django.views.generic import TemplateView

from .models import Prices


class iPhone(BaseLineChartView):

    table = (
        Prices.objects.filter(product_number="5594641")
        .annotate(date=TruncDate("timestamp"))
        .values("date", "seller_name", "price_excl_shipping")
    )

    table_pd = pd.DataFrame(
        {
            "date": [elm["date"] for elm in table],
            "seller_name": [elm["seller_name"] for elm in table],
            "price_excl_shipping": [elm["price_excl_shipping"] for elm in table],
        }
    )

    table_pd.sort_values(["seller_name", "date"], inplace=True)

    def get_labels(self):
        """ Unique date labels """
        dates = self.table_pd.date.unique()
        return [now.strftime("%m/%d/%Y") for now in dates]

    def get_providers(self):
        """ Unique retailers """
        return self.table_pd.seller_name.unique()

    def get_data(self):
        """ Prices per day per retailer """
        return [
            list(
                self.table_pd[
                    self.table_pd.seller_name == seller_name
                ].price_excl_shipping.values
            )
            for seller_name in self.get_providers()
        ]


line_chart = TemplateView.as_view(template_name="charts.html")
line_chart_json = iPhone.as_view()
