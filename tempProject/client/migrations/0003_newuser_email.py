# Generated by Django 5.0.3 on 2024-03-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_remove_newuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='email address'),
        ),
    ]
