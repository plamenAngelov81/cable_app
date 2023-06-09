# Generated by Django 4.2 on 2023-04-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cable', '0002_order_alter_cable_options_alter_cable_cable_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='confirm_user',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='is_confirmed',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='cable_quantity',
            field=models.PositiveIntegerField(verbose_name='Quantity'),
        ),
    ]
