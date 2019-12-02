# Generated by Django 2.2.7 on 2019-11-20 06:47

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('titleko', models.CharField(max_length=128, verbose_name='소개타이틀(한국어)')),
                ('titleeng', models.CharField(max_length=128, verbose_name='소개타이틀(영어)')),
                ('titleven', models.CharField(max_length=128, verbose_name='소개타이틀(베트남어)')),
                ('created', models.DateField(verbose_name='Created')),
                ('picture1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture1')),
                ('picture2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture2')),
                ('picture3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture3')),
                ('picture4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture4')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Rocation')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'db_table': 'city',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='InfoTravel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyko', models.CharField(max_length=64, verbose_name='업체명(한국어)')),
                ('companyeng', models.CharField(max_length=64, verbose_name='업체명(영어)')),
                ('companyven', models.CharField(max_length=64, verbose_name='업체명(베트남어)')),
                ('picture1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture2')),
                ('picture2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture2')),
                ('picture3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture2')),
                ('picture4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture2')),
                ('part', models.CharField(choices=[('EatDrink', '먹다/마시다'), ('See', '보다'), ('Sleep', '자다'), ('Buy', '사다')], max_length=64, verbose_name='구분')),
                ('typeit', models.IntegerField(choices=[(1, 'Must See'), (2, 'Hot')], verbose_name='유형선택')),
                ('addressko', models.CharField(max_length=128, verbose_name='주소(한국어)')),
                ('addresseng', models.CharField(max_length=128, verbose_name='주소(영어)')),
                ('addressven', models.CharField(max_length=128, verbose_name='주소(베트남어)')),
                ('category', models.CharField(choices=[(1, 'Place'), (2, '랜드마크'), (3, '자연'), (4, '공원'), (5, '박물관'), (6, '종교'), (7, '거\x1f리'), (8, '시장'), (9, '교통'), (10, '공공')], max_length=8, verbose_name='카테고리')),
                ('linkweb', models.CharField(blank=True, max_length=64, null=True, verbose_name='외부링크(웹사이트)')),
                ('linkinsta', models.CharField(blank=True, max_length=64, null=True, verbose_name='외부링크(인스타그램)')),
                ('linkyoutube', models.CharField(blank=True, max_length=64, null=True, verbose_name='외부링크(유튜브)')),
                ('trafficko', models.CharField(blank=True, max_length=128, null=True, verbose_name='교통정보(한국어)')),
                ('trafficeng', models.CharField(blank=True, max_length=128, null=True, verbose_name='교통정보(영어)')),
                ('trafficven', models.CharField(blank=True, max_length=128, null=True, verbose_name='교통정보(베트남어)')),
                ('introko', models.TextField(blank=True, help_text='이곳을 소개해 주세요.', null=True, verbose_name='소개정보(한국어)')),
                ('introeng', models.TextField(blank=True, help_text='이곳을 소개해 주세요.', null=True, verbose_name='소개정보(영어)')),
                ('introven', models.TextField(blank=True, help_text='이곳을 소개해 주세요.', null=True, verbose_name='소개정보(베트남어)')),
                ('itdate', models.DateField(verbose_name='Date')),
                ('itlocation', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Rocation')),
            ],
            options={
                'verbose_name': 'InfoTravel',
                'verbose_name_plural': 'InfoTravels',
                'db_table': 'infotravel',
            },
        ),
        migrations.CreateModel(
            name='SecondTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThirdTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThirdTaggedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travels_thirdtaggeditem_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travels_thirdtaggeditem_items', to='travels.ThirdTag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SleepPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inclusionko', models.CharField(max_length=64, verbose_name='포함사항(한국어)')),
                ('inclusioneng', models.CharField(max_length=64, verbose_name='포함사항(영어)')),
                ('inclusionven', models.CharField(max_length=64, verbose_name='포함사항(베트남어)')),
                ('roomtypeko', models.CharField(max_length=64, verbose_name='객실타입(한국어)')),
                ('roomtypeeng', models.CharField(max_length=64, verbose_name='객실타입(영어)')),
                ('roomtypeven', models.CharField(max_length=64, verbose_name='객실타입(베트남어)')),
                ('part', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='travels.InfoTravel')),
            ],
        ),
        migrations.CreateModel(
            name='SeePart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operationtimeko', models.CharField(max_length=64, verbose_name='운영시간(한국어)')),
                ('operationtimeeng', models.CharField(max_length=64, verbose_name='운영시간(영어)')),
                ('operationtimeven', models.CharField(max_length=64, verbose_name='운영시간(베트남어)')),
                ('part', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='travels.InfoTravel')),
            ],
        ),
        migrations.CreateModel(
            name='SecondTaggedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travels_secondtaggeditem_tagged_items', to='contenttypes.ContentType', verbose_name='Content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travels_secondtaggeditem_items', to='travels.SecondTag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='infotravel',
            name='tageng',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='travels.SecondTaggedItem', to='travels.SecondTag', verbose_name='태그(영어)'),
        ),
        migrations.AddField(
            model_name='infotravel',
            name='tagko',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='태그(한국어)'),
        ),
        migrations.AddField(
            model_name='infotravel',
            name='tagven',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='travels.ThirdTaggedItem', to='travels.ThirdTag', verbose_name='태그(베트남어)'),
        ),
        migrations.CreateModel(
            name='EatDrinkPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biztimeko', models.CharField(max_length=64, verbose_name='영업시간(한국어)')),
                ('biztimeeng', models.CharField(max_length=64, verbose_name='영업시간(영어)')),
                ('biztimeven', models.CharField(max_length=64, verbose_name='영업시간(베트남어)')),
                ('menuko', models.CharField(max_length=64, verbose_name='영업시간(한국어)')),
                ('menueng', models.CharField(max_length=64, verbose_name='영업시간(영어)')),
                ('menuven', models.CharField(max_length=64, verbose_name='영업시간(베트남어)')),
                ('part', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='travels.InfoTravel')),
            ],
        ),
        migrations.CreateModel(
            name='BuyPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biztimeko', models.CharField(max_length=64, verbose_name='영업시간(한국어)')),
                ('biztimeeng', models.CharField(max_length=64, verbose_name='영업시간(영어)')),
                ('biztimeven', models.CharField(max_length=64, verbose_name='영업시간(베트남어)')),
                ('saleitemsko', models.CharField(max_length=64, verbose_name='판매상품(한국어)')),
                ('saleitemseng', models.CharField(max_length=64, verbose_name='판매상품(영어)')),
                ('saleitemsven', models.CharField(max_length=64, verbose_name='판매상품(베트남어)')),
                ('part', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='travels.InfoTravel')),
            ],
        ),
    ]
