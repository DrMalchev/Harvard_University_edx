# Generated by Django 3.2.6 on 2021-09-14 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_listings_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.IntegerField(choices=[('Fashion', 'Fashion'), ('Toys', 'Toys'), ('Electronics', 'Electronics'), ('Home', 'Home'), ('Other', 'Other')]),
        ),
    ]