# Generated by Django 5.0.3 on 2024-04-23 18:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0017_auto_20240423_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked',
            name='bookedID',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='customerlist',
            name='customerID',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
