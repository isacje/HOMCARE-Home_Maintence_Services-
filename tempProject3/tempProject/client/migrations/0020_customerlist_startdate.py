# Generated by Django 5.0.3 on 2024-04-23 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0019_booked_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerlist',
            name='startDate',
            field=models.DateField(default='2024-04-24'),
        ),
    ]