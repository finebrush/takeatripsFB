# Generated by Django 2.2.7 on 2019-12-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ARTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleko', models.CharField(max_length=128, verbose_name='소개타이틀(한국어)')),
                ('titleeng', models.CharField(max_length=128, verbose_name='소개타이틀(영어)')),
                ('titleven', models.CharField(max_length=128, verbose_name='소개타이틀(베트남어)')),
                ('created', models.DateField(verbose_name='Created')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Picture')),
                ('category', models.CharField(choices=[(1, '문화유적'), (2, '랜드마크'), (3, '거리'), (4, '공원'), (5, '박물관'), (6, '종교'), (7, '자연'), (8, '시장'), (9, '교통'), (10, '공공'), (11, 'Place')], max_length=64, verbose_name='구분')),
            ],
            options={
                'verbose_name': 'ARTrip',
                'verbose_name_plural': 'ARTrip',
                'db_table': 'artrip',
                'ordering': ('titleko',),
            },
        ),
    ]
