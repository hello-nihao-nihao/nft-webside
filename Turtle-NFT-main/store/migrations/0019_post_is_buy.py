# Generated by Django 4.1.2 on 2023-03-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_remove_profile_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_buy',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]
