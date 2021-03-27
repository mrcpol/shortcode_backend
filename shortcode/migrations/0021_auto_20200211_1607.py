# Generated by Django 3.0.2 on 2020-02-11 16:07

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shortcode', '0020_auto_20200207_0414'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductChangeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(db_index=True, max_length=31, verbose_name='SKU')),
                ('prev_data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Previous Product Data')),
                ('new_data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='New Product Data')),
                ('fields', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=63), blank=True, size=None)),
            ],
        ),
        migrations.AddField(
            model_name='eventlog',
            name='event_state',
            field=models.IntegerField(choices=[(0, 'Started'), (1, 'Completed')], default=0),
        ),
        migrations.AlterField(
            model_name='field',
            name='field_type',
            field=models.IntegerField(choices=[(0, 'Data'), (1, 'Shortcode'), (2, 'Result')], default=0),
        ),
        migrations.AlterField(
            model_name='usersetting',
            name='size_shortcode',
            field=models.IntegerField(default=11, verbose_name='Font Size for the ShortCode'),
        ),
        migrations.DeleteModel(
            name='UserLog',
        ),
        migrations.AddField(
            model_name='productchangelog',
            name='event_log',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shortcode.EventLog', verbose_name='EventLog'),
        ),
        migrations.AddField(
            model_name='productchangelog',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
