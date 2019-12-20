# Generated by Django 2.2.7 on 2019-12-13 23:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travels', '0024_auto_20191213_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liketc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('travelcurator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travels.TravelCurator')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'travelcurator')},
            },
        ),
        migrations.AddField(
            model_name='travelcurator',
            name='like_travelcurator',
            field=models.ManyToManyField(blank=True, related_name='like_travelcurator', through='travels.Liketc', to=settings.AUTH_USER_MODEL),
        ),
    ]