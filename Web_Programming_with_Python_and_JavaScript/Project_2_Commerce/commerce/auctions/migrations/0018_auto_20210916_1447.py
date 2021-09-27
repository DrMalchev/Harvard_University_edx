# Generated by Django 3.2.6 on 2021-09-16 11:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auto_20210916_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.CharField(default=None, max_length=256),
        ),
        migrations.AddField(
            model_name='comments',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='time',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]