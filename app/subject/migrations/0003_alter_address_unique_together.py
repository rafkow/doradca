# Generated by Django 4.2.4 on 2023-10-29 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_rename_adress_address'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='address',
            unique_together={('street', 'house_number', 'city', 'postcode')},
        ),
    ]
