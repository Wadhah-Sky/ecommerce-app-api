# Generated by Django 4.0.10 on 2023-04-25 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_rename_use_attribute_img_product_use_item_attribute_color_shape_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='stock',
            field=models.PositiveSmallIntegerField(default=10),
        ),
    ]