# Generated by Django 3.1.6 on 2021-02-25 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20210225_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='image_url',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='URL de l’image'),
        ),
    ]
