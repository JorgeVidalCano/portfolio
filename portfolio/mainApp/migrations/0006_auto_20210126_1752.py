# Generated by Django 3.1.4 on 2021-01-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_auto_20210126_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutdata',
            name='sideImg',
            field=models.ImageField(blank=True, upload_to='Images'),
        ),
        migrations.AlterField(
            model_name='homedata',
            name='mainImg',
            field=models.ImageField(blank=True, upload_to='Images'),
        ),
    ]
