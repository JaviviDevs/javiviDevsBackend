# Generated by Django 5.0 on 2023-12-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asociations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asociation',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
