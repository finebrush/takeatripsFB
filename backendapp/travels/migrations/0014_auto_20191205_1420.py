# Generated by Django 2.2.7 on 2019-12-05 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0013_auto_20191205_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotravel',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Picture1'),
        ),
        migrations.AlterField(
            model_name='infotravel',
            name='picture10',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Picture10'),
        ),
        migrations.AlterField(
            model_name='infotravel',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Picture2'),
        ),
        migrations.AlterField(
            model_name='infotravel',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Picture3'),
        ),
        migrations.AlterField(
            model_name='infotravel',
            name='picture4',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Picture4'),
        ),
        migrations.AlterField(
            model_name='infotravel',
            name='picture5',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Picture5'),
        ),
        migrations.AlterField(
            model_name='infotravel',
            name='picture6',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Picture6'),
        ),
        migrations.AlterField(
            model_name='infotravel',
            name='picture7',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Picture7'),
        ),
        migrations.AlterField(
            model_name='infotravel',
            name='picture8',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Picture8'),
        ),
        migrations.AlterField(
            model_name='infotravel',
            name='picture9',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Picture9'),
        ),
        migrations.AlterField(
            model_name='poipoint',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Picture1'),
        ),
        migrations.AlterField(
            model_name='poipoint',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Picture2'),
        ),
        migrations.AlterField(
            model_name='poipoint',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Picture3'),
        ),
        migrations.AlterField(
            model_name='poipoint',
            name='picture4',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Picture4'),
        ),
        migrations.AlterField(
            model_name='tcimage',
            name='tcimg',
            field=models.ImageField(upload_to='%Y/%m/%d', verbose_name='Trave Image'),
        ),
    ]
