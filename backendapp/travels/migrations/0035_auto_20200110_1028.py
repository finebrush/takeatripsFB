# Generated by Django 2.2.7 on 2020-01-10 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0034_auto_20200110_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotravel',
            name='picture1',
            field=models.ImageField(default='', upload_to='%Y/%m/%d', verbose_name='Picture1'),
        ),
    ]