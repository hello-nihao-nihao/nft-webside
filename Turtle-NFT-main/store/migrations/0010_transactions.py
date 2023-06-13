# Generated by Django 4.1.2 on 2022-10-12 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord_link', models.CharField(max_length=500, null=True)),
                ('wallet_address', models.CharField(max_length=10000, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
