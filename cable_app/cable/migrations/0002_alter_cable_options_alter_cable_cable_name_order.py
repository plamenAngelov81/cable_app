# Generated by Django 4.2 on 2023-04-25 14:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cable', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cable',
            options={'ordering': ['pk']},
        ),
        migrations.AlterField(
            model_name='cable',
            name='cable_name',
            field=models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Cable Name'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cable_quantity', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('cable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cable.cable')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
