# Generated by Django 3.1.5 on 2021-01-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20210122_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='base_domain',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='domaine'),
        ),
        migrations.AlterField(
            model_name='source',
            name='base_domain',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='domaine'),
        ),
    ]