# Generated by Django 5.0.3 on 2024-03-24 12:31


from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_remove_newuser_email_alter_newuser_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceprovider',
            name='clinetID',
        ),
        migrations.AddField(
            model_name='newuser',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='clientID',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='userID',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='password',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]