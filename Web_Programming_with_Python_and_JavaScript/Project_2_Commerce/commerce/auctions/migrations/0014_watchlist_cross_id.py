# Generated by Django 3.2.6 on 2021-09-16 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20210915_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='cross_id',
            field=models.IntegerField(default=None, max_length=64),
        ),
    ]
