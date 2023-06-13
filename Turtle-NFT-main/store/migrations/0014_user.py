# Generated by Django 4.1.2 on 2023-03-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0013_rename_blockash_transaction_block_hash"),
    ]

    operations = [
        migrations.CreateModel(
            name="user",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("account", models.CharField(max_length=50, verbose_name="account")),
                ("password", models.CharField(max_length=50, verbose_name="password")),
            ],
            options={
                "db_table": "user_login",
            },
        ),
    ]
