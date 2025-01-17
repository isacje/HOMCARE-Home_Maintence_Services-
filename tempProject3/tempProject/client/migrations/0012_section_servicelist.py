# Generated by Django 5.0.3 on 2024-04-17 03:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_serviceprovider_pan_serviceprovider_panname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employeeCount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=350)),
                ('employeePerArea', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timeToComplete', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sectionType', models.CharField(max_length=20)),
                ('sectionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.serviceprovider')),
            ],
        ),
        migrations.CreateModel(
            name='serviceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(max_length=20)),
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.serviceprovider')),
            ],
        ),
    ]
