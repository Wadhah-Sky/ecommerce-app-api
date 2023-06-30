# Generated by Django 4.0.10 on 2023-05-20 14:17

from django.db import migrations
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_purchaseorder_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poshipping',
            name='cost',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=8, validators=[djmoney.models.validators.MinMoneyValidator({'USD': 0})]),
        ),
    ]
