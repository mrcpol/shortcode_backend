# Generated by Django 3.0.2 on 2020-06-26 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortcode', '0028_auto_20200227_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='modified',
            field=models.BooleanField(default=False, verbose_name='Product Data Updated?'),
        ),
    ]
