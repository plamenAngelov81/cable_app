# Generated by Django 4.2 on 2023-05-03 13:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cable', '0004_alter_cable_machine_alter_order_is_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cable',
            name='inductor_type',
            field=models.TextField(max_length=200, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Inductor Type'),
        ),
    ]
