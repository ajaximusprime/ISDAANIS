# Generated by Django 4.2.1 on 2023-07-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analytics', '0003_remove_dailytransaction_user_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailytransaction',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='dailytransaction',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dailytransaction',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
