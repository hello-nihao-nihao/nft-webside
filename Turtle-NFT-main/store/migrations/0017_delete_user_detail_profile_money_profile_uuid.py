# Generated by Django 4.1.2 on 2023-03-22 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_remove_profile_id_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_detail',
        ),
        migrations.AddField(
            model_name='profile',
            name='money',
            field=models.FloatField(default=0.0, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='uuid',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
