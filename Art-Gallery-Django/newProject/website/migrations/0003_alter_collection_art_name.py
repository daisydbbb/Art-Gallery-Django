# Generated by Django 5.0 on 2023-12-08 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0002_collection_art_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collection",
            name="art_name",
            field=models.CharField(max_length=100),
        ),
    ]