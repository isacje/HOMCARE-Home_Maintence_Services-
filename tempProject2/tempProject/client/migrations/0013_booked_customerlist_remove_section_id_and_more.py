# Generated by Django 5.0.3 on 2024-04-23 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_section_servicelist'),
    ]

    operations = [
        migrations.CreateModel(
            name='booked',
            fields=[
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='client.client')),
                ('companyName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='email address')),
                ('phoneNo', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('officeAddress', models.CharField(max_length=50)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='customerList',
            fields=[
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='client.serviceprovider')),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('phoneNo', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='section',
            name='id',
        ),
        migrations.RemoveField(
            model_name='servicelist',
            name='id',
        ),
        migrations.AlterField(
            model_name='section',
            name='sectionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='client.serviceprovider'),
        ),
        migrations.AlterField(
            model_name='servicelist',
            name='ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='client.serviceprovider'),
        ),
    ]
