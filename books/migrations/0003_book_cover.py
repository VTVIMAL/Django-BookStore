# Generated by Django 4.1.3 on 2022-11-11 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="cover",
            field=models.ImageField(blank=True, upload_to="covers/"),
        ),
    ]
