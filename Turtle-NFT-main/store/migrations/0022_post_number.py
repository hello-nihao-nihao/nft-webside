# Generated by Django 4.1.2 on 2023-04-01 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0021_post_owner_alter_post_is_buy"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="number",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
