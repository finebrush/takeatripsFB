# Generated by Django 2.2.7 on 2019-12-17 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0026_auto_20191215_0310'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='gotocity',
            field=models.CharField(choices=[(1, 'Seoul'), (2, 'Busan')], max_length=64, null=True, verbose_name='Select City'),
        ),
    ]