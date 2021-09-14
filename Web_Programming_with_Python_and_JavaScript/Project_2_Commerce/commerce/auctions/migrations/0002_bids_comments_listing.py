# Generated by Django 3.2.6 on 2021-09-14 07:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=124)),
                ('starting_bid', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('image_url', models.URLField(max_length=124)),
                ('category', models.IntegerField(choices=[(1, 'Fashion'), (2, 'Toys'), (3, 'Electronics'), (4, 'Home'), (5, 'Other')])),
                ('comment', models.CharField(max_length=124)),
                ('new_bid', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
            ],
        ),
    ]
