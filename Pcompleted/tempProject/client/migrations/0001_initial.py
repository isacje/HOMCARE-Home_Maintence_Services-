# Generated by Django 5.0.3 on 2024-03-24 08:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(blank=True, max_length=150)),
                ('phoneNo', models.CharField(max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('newuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('userID', models.CharField(max_length=20, unique=True)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('client.newuser',),
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('newuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('clinetID', models.CharField(max_length=20, unique=True)),
                ('companyName', models.CharField(max_length=50)),
                ('ownerName', models.CharField(max_length=30)),
                ('officeAddress', models.CharField(max_length=50)),
                ('gstNo', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('client.newuser',),
        ),
    ]