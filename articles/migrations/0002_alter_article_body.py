# Generated by Django 4.2 on 2023-05-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="body",
            field=models.TextField(),
        ),
    ]
