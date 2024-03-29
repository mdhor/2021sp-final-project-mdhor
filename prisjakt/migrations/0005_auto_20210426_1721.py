# Generated by Django 3.2 on 2021-04-26 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prisjakt", "0004_prices_timestamp"),
    ]

    operations = [
        migrations.AddField(
            model_name="prices",
            name="unique_identifier",
            field=models.CharField(
                default="dummy", max_length=100, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="prices",
            name="price_id",
            field=models.IntegerField(null=True),
        ),
    ]
