# Generated by Django 3.1.4 on 2021-01-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstParagraph', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('country', models.CharField(max_length=8)),
                ('education', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=35)),
                ('extraInfobotoom', models.CharField(max_length=300)),
                ('skillText', models.CharField(max_length=300)),
            ],
        ),
    ]
