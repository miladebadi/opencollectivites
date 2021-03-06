# Generated by Django 3.1.6 on 2021-02-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20210212_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='image_url',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='URL d’illustration'),
        ),
        migrations.AddField(
            model_name='document',
            name='weight',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='poids'),
        ),
    ]
