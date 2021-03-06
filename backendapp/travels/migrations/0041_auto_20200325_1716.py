# Generated by Django 2.2.7 on 2020-03-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0020_auto_20200325_1716'),
        ('travels', '0040_auto_20200325_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buypart',
            name='pin',
        ),
        migrations.AddField(
            model_name='buypart',
            name='pin',
            field=models.ManyToManyField(to='common.PinBuy', verbose_name='사다 핀'),
        ),
        migrations.RemoveField(
            model_name='drinkpart',
            name='pin',
        ),
        migrations.AddField(
            model_name='drinkpart',
            name='pin',
            field=models.ManyToManyField(to='common.PinDrink', verbose_name='마시다 핀'),
        ),
        migrations.RemoveField(
            model_name='eatpart',
            name='pin',
        ),
        migrations.AddField(
            model_name='eatpart',
            name='pin',
            field=models.ManyToManyField(to='common.PinEat', verbose_name='먹다 핀'),
        ),
        migrations.RemoveField(
            model_name='funpart',
            name='pin',
        ),
        migrations.AddField(
            model_name='funpart',
            name='pin',
            field=models.ManyToManyField(to='common.PinFun', verbose_name='놀다 핀'),
        ),
        migrations.AlterField(
            model_name='infotravel',
            name='part',
            field=models.CharField(choices=[('Eat', '먹다'), ('Drink', '마시다'), ('Fun', '놀다'), ('Sleep', '자다'), ('Buy', '사다')], max_length=64, verbose_name='구분'),
        ),
    ]
