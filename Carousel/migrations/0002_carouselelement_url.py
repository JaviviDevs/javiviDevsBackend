# Generated by Django 5.0 on 2023-12-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carousel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselelement',
            name='url',
            field=models.CharField(default='', max_length=100),
        ),
    ]
