# Generated by Django 4.1.2 on 2023-04-05 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0029_rename_user_post_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="price",
        ),
    ]
