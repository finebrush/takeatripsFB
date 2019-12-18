# Generated by Django 2.2.7 on 2019-12-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0020_auto_20191213_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='nameeng',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Name(영어)'),
        ),
        migrations.AlterField(
            model_name='city',
            name='nameko',
            field=models.CharField(default=None, max_length=64, verbose_name='Name(한국어)'),
        ),
        migrations.AlterField(
            model_name='city',
            name='nameven',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Name(베트남어)'),
        ),
    ]
