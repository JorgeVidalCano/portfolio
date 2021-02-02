# Generated by Django 3.1.4 on 2021-02-01 18:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_skilldata'),
    ]

    operations = [
        migrations.AddField(
            model_name='skilldata',
            name='percentaje',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
            preserve_default=False,
        ),
    ]
