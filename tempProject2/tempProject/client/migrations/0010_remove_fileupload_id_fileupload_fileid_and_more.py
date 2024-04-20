# Generated by Django 5.0.3 on 2024-04-03 18:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_fileupload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='id',
        ),
        migrations.AddField(
            model_name='fileupload',
            name='fileID',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='field_name',
            field=models.FileField(max_length=254, upload_to='C:/Users/Dell/Documents/temp/tempProject/media'),
        ),
    ]
