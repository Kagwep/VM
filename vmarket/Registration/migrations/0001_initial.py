# Generated by Django 3.2.9 on 2022-02-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=100, verbose_name='enter first name')),
                ('last_name', models.CharField(max_length=100, verbose_name='enter last name')),
                ('email', models.EmailField(max_length=254, verbose_name='enter last name')),
                ('phone_number', models.CharField(max_length=20, unique=True, verbose_name='enter valid phone number')),
                ('category', models.CharField(max_length=20, verbose_name='sing up as ')),
                ('Shop_name', models.CharField(max_length=200, verbose_name='enter shop name')),
                ('commodities', models.CharField(max_length=200, verbose_name='Shop category')),
                ('location', models.CharField(max_length=200, verbose_name='Shops location')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
