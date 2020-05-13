# Generated by Django 2.2.7 on 2020-05-10 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0050_auto_20200428_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='poipoint',
            name='ptitleeng',
            field=models.CharField(max_length=256, null=True, verbose_name='설명(영어)'),
        ),
        migrations.AddField(
            model_name='poipoint',
            name='ptitleko',
            field=models.CharField(max_length=256, null=True, verbose_name='설명(한국어)'),
        ),
        migrations.AddField(
            model_name='poipoint',
            name='ptitleven',
            field=models.CharField(max_length=4256, null=True, verbose_name='설명(베트남어)'),
        ),
        migrations.AlterField(
            model_name='infotravel',
            name='typeit',
            field=models.IntegerField(choices=[(1, 'Must'), (2, 'Hot'), (3, 'Normal')], verbose_name='유형선택'),
        ),
    ]
