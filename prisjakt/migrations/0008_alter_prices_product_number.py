# Generated by Django 3.2 on 2021-04-26 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prisjakt", "0007_alter_prices_unique_identifier"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prices",
            name="product_number",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="prisjakt.products"
            ),
        ),
    ]
