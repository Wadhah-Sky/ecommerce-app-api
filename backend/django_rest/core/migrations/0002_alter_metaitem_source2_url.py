# Generated by Django 4.0.10 on 2024-01-29 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metaitem',
            name='source2_url',
            field=models.URLField(blank=True, help_text='You can set URL for icon image source e.g. PNG or JPG, currently this one being used', max_length=255),
        ),
    ]
