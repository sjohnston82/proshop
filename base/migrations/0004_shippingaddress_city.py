# Generated by Django 3.1.6 on 2021-02-27 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
