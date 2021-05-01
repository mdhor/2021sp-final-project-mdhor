import matplotlib.pyplot as plt
import mpld3
import pandas as pd
import seaborn as sns
from django.db.models import Max
from django.db.models.functions import TruncDate
from django.http import HttpResponse

from .models import Prices


def iphone_line(request):
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

    cheapest_retailers = (
        table_pd[table_pd.date == table_pd.date.unique().max()]
        .nsmallest(10, "price_excl_shipping")
        .seller_name
    )
    table_pd = table_pd[table_pd.seller_name.isin(cheapest_retailers)]

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.lineplot(
        x="date", y="price_excl_shipping", hue="seller_name", data=table_pd, ax=ax
    )
    plt.legend(loc="upper left")
    pl_html = mpld3.fig_to_html(fig)
    return HttpResponse(pl_html)


def iphone_scatter(request):
    table = (
        Prices.objects.filter(product_number="5594641")
        .filter(timestamp=Prices.objects.aggregate(Max("timestamp"))["timestamp__max"])
        .values("seller_rating", "seller_name", "price_excl_shipping")
    )

    table_pd = pd.DataFrame(
        {
            "seller_rating": [elm["seller_rating"] for elm in table],
            "seller_name": [elm["seller_name"] for elm in table],
            "price_excl_shipping": [elm["price_excl_shipping"] for elm in table],
        }
    ).dropna()

    fig, ax = plt.subplots(figsize=(20, 10))
    g = ax.scatter(table_pd.seller_rating, table_pd.price_excl_shipping, s=100)
    labels = [f"Retailer: {retailer}" for retailer in table_pd.seller_name]
    tooltip = mpld3.plugins.PointLabelTooltip(g, labels=labels)
    mpld3.plugins.connect(fig, tooltip)

    pl_html = mpld3.fig_to_html(fig)
    return HttpResponse(pl_html)
