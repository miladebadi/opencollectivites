# Generated by Django 3.1.5 on 2021-01-22 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20210122_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('name', models.CharField(max_length=100, verbose_name='nom')),
                ('acronym', models.CharField(max_length=100, verbose_name='sigle')),
                ('logo', models.ImageField(blank=True, upload_to='logos')),
            ],
            options={
                'verbose_name': 'éditeur',
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Editor',
        ),
        migrations.AlterField(
            model_name='source',
            name='editor',
            field=models.ManyToManyField(to='core.Organization', verbose_name='éditeur'),
        ),
    ]
