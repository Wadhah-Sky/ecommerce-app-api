# Generated by Django 4.0.10 on 2023-03-25 01:36

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_product_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='details',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True),
        ),
    ]