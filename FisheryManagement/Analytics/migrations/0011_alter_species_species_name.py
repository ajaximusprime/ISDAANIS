# Generated by Django 4.2.1 on 2024-01-08 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analytics', '0010_dailytransaction_unloadtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='species_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
