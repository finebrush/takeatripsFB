# Generated by Django 2.2.7 on 2019-11-20 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_tmpadd_has_submenu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tmpadd',
            name='has_submenu',
        ),
        migrations.AlterField(
            model_name='tmpadd',
            name='tmptest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.TmpTest'),
        ),
    ]