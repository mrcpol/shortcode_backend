# Generated by Django 3.0.2 on 2020-02-07 04:14

from django.db import migrations, models
import shortcode.models


class Migration(migrations.Migration):

    dependencies = [
        ('shortcode', '0019_usersetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersetting',
            name='size_shortcode',
            field=models.IntegerField(default=14, verbose_name='Font Size for the ShortCode'),
        ),
        migrations.AlterField(
            model_name='usersetting',
            name='color_background',
            field=shortcode.models.ColorField(default='#ffffff', max_length=10, verbose_name='Color for the Background'),
        ),
        migrations.AlterField(
            model_name='usersetting',
            name='color_dropdown',
            field=shortcode.models.ColorField(default='#ffffff', max_length=10, verbose_name='Color for Dropdown'),
        ),
    ]
