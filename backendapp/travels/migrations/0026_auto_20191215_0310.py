# Generated by Django 2.2.7 on 2019-12-14 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travels', '0025_auto_20191214_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liketp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('travelplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travels.TravelPlan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'travelplan')},
            },
        ),
        migrations.AddField(
            model_name='travelplan',
            name='like_travelplan',
            field=models.ManyToManyField(blank=True, related_name='like_travelplan', through='travels.Liketp', to=settings.AUTH_USER_MODEL),
        ),
    ]