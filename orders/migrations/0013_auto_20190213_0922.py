# Generated by Django 2.0.3 on 2019-02-13 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]