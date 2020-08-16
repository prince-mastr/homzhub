# Generated by Django 2.2.4 on 2020-08-16 12:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200816_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='Remarks',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='phone',
            field=models.IntegerField(default=1000000000, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='request',
            name='pincode',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(100000)]),
        ),
    ]
