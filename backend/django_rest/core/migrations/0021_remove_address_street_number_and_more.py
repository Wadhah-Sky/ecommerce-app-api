# Generated by Django 4.0.10 on 2023-05-16 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_productitem_limit_per_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='street_number',
        ),
        migrations.RemoveField(
            model_name='address',
            name='unit_number',
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='Addresses_country', to='core.country'),
        ),
    ]
