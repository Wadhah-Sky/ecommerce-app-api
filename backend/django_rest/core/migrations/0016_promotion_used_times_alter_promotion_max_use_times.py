# Generated by Django 4.0.10 on 2023-05-10 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_rename_use_times_promotion_max_use_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='used_times',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='max_use_times',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
