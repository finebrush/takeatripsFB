# Generated by Django 2.2.7 on 2019-12-16 08:43

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcontent', '0006_arlocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='artrip',
            name='arlocation',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='위치'),
        ),
        migrations.DeleteModel(
            name='ARLocation',
        ),
    ]
