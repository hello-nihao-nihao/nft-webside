# Generated by Django 4.1.2 on 2023-03-22 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_delete_user_detail_profile_money_profile_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='uuid',
        ),
    ]
