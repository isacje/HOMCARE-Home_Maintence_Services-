# Generated by Django 5.0.3 on 2024-04-03 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_newuser_is_active_newuser_is_staff_newuser_usertype_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='fileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.FileField(max_length=254, upload_to='C:/Users/Dell/Desktop/uploads')),
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.serviceprovider')),
            ],
        ),
    ]