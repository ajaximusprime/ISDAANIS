# Generated by Django 4.2.1 on 2023-12-17 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analytics', '0007_unloadtype_alter_origin_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='origin',
            name='percentage',
        ),
        migrations.RemoveField(
            model_name='origin',
            name='volume',
        ),
        migrations.AddField(
            model_name='dailytransaction',
            name='percentage',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
