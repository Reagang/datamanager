# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-28 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("budgetportal", "0030_auto_20190821_2046")]

    operations = [
        migrations.AlterField(
            model_name="infrastructureprojectpart",
            name="financial_year",
            field=models.CharField(max_length=4),
        )
    ]
