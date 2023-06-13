# Generated by Django 4.1.2 on 2023-04-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0022_post_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="last_uuid",
            field=models.CharField(default="none", max_length=100),
        ),
        migrations.AlterField(
            model_name="post",
            name="number",
            field=models.CharField(default=1, max_length=100),
        ),
    ]