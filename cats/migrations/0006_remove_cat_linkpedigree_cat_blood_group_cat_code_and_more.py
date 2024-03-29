# Generated by Django 5.0 on 2024-02-08 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0005_photoscat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='linkPedigree',
        ),
        migrations.AddField(
            model_name='cat',
            name='blood_group',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='cat',
            name='code',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='cat',
            name='color',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='cat',
            name='father_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='cat',
            name='link_pedigree',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='cat',
            name='mother_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='cat',
            name='test',
            field=models.CharField(default='', max_length=255),
        ),
    ]
