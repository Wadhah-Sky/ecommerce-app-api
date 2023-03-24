# Generated by Django 4.0.8 on 2023-03-18 23:08

import core.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_attribute_input_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=core.models.create_image_file_path),
        ),
    ]