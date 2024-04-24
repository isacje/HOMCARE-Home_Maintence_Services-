# Generated by Django 5.0.3 on 2024-04-23 19:40

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_section_servicelist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='id',
        ),
        migrations.RemoveField(
            model_name='servicelist',
            name='id',
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='field_name',
            field=models.FileField(max_length=254, upload_to='C:/Users/Vivobook/Desktop/FM/Mini/tempProject2/tempProject/media'),
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
        migrations.CreateModel(
            name='booked',
            fields=[
                ('bookedID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('companyName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='email address')),
                ('phoneNo', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('officeAddress', models.CharField(max_length=50)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('status', models.CharField(max_length=20)),
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='customerList',
            fields=[
                ('customerID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='email address')),
                ('username', models.CharField(max_length=150)),
                ('phoneNo', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.serviceprovider')),
            ],
        ),
    ]
