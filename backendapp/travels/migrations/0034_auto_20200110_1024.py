# Generated by Django 2.2.7 on 2020-01-10 01:24

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0033_auto_20200105_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotravel',
            name='addresseng',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='주소(영어)'),
        ),
        migrations.AlterField(
            model_name='infotravel',
            name='addressven',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='주소(베트남어)'),
        ),
        migrations.AlterField(
            model_name='infotravel',
            name='tageng',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='travels.SecondTaggedItem', to='travels.SecondTag', verbose_name='태그(영어)'),
        ),
        migrations.AlterField(
            model_name='infotravel',
            name='tagko',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='태그(한국어)'),
        ),
        migrations.AlterField(
            model_name='infotravel',
            name='tagven',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='travels.ThirdTaggedItem', to='travels.ThirdTag', verbose_name='태그(베트남어)'),
        ),
    ]
