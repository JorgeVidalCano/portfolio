# Generated by Django 3.1.4 on 2021-01-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20210125_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutdata',
            name='sideImg',
            field=models.ImageField(blank=True, upload_to='postImages'),
        ),
        migrations.AddField(
            model_name='homedata',
            name='mainImg',
            field=models.ImageField(blank=True, upload_to='postImages'),
        ),
    ]