# Generated by Django 2.2.7 on 2020-03-25 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0018_auto_20200325_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pinbuy',
            name='nameeng',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='pinbuy',
            name='nameven',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='pindrink',
            name='nameeng',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='pindrink',
            name='nameven',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='pineat',
            name='nameeng',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='pineat',
            name='nameven',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='pinfun',
            name='nameeng',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='pinfun',
            name='nameven',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
