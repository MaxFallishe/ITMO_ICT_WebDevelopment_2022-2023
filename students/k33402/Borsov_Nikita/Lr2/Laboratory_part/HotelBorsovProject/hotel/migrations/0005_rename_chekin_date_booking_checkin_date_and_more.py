# Generated by Django 4.1.7 on 2023-03-13 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_alter_booking_chekin_date_alter_booking_chekout_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='chekin_date',
            new_name='checkin_date',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='chekout_date',
            new_name='checkout_date',
        ),
    ]
