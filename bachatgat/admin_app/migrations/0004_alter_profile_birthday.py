# Generated by Django 4.2.1 on 2023-08-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_profile_address_profile_birthday_profile_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(default=''),
        ),
    ]