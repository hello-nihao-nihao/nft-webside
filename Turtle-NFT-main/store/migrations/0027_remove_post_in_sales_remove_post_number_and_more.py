# Generated by Django 4.1.2 on 2023-04-04 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0026_post_old_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="in_sales",
        ),
        migrations.RemoveField(
            model_name="post",
            name="number",
        ),
        migrations.RemoveField(
            model_name="post",
            name="old_price",
        ),
    ]
