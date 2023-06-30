# Generated by Django 4.0.10 on 2023-06-19 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_remove_purchaseorder_tax'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryTax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_tax_country', to='core.country')),
                ('tax', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_tax_tax', to='core.tax')),
            ],
        ),
        migrations.AddConstraint(
            model_name='countrytax',
            constraint=models.UniqueConstraint(fields=('country', 'tax'), name='country_tax_unique_appversion'),
        ),
    ]
