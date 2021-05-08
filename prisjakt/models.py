from datetime import datetime

from django.db import models


class Products(models.Model):
    product_number = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50, null=True)


class Prices(models.Model):
    price_id = models.IntegerField(null=True)
    seller_product_name = models.CharField(max_length=50, null=True)
    stock_status = models.CharField(max_length=50, null=True)
    price_incl_shipping = models.FloatField(null=True)
    price_excl_shipping = models.FloatField(null=True)
    seller_id = models.IntegerField()
    seller_name = models.CharField(max_length=50, null=True)
    seller_rating = models.FloatField(null=True)
    product_number = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    unique_identifier = models.CharField(primary_key=True, max_length=100)
