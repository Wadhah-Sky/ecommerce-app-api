# Generated by Django 4.0.10 on 2023-03-26 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_productitem_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productitemimage',
            old_name='thumbnail',
            new_name='image',
        ),
    ]