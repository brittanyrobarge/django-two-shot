# Generated by Django 5.0 on 2023-12-18 22:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expensecategory",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
