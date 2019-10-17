# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-15 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("budgetportal", "0024_remove-infraproject-fields")]

    operations = [
        migrations.AddField(
            model_name="infrastructureprojectpart",
            name="amount",
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="infrastructureprojectpart",
            name="financial_year",
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="infrastructureprojectpart",
            name="total_project_cost",
            field=models.BigIntegerField(default=0),
        ),
    ]
