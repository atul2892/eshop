# Generated by Django 4.1.2 on 2022-12-07 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_checkout_orderstatus_checkout_paymentstatus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutproducts',
            name='qty',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='checkoutproducts',
            name='total',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
