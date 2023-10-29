# Generated by Django 4.0.10 on 2023-10-21 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_topbanner_summary_alter_topbanner_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='topbanner',
            name='url_target',
            field=models.CharField(choices=[('_self', '_self'), ('_blank', '_blank'), ('_parent', '_parent'), ('_top', '_top')], default='_blank', max_length=7),
        ),
    ]
