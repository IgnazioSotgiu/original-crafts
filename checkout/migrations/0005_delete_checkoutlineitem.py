# Generated by Django 3.2.6 on 2021-09-18 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_checkoutlineitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CheckoutLineItem',
        ),
    ]
