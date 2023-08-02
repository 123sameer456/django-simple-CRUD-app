# Generated by Django 4.1.7 on 2023-05-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("Student_Name", models.CharField(max_length=70)),
                ("Father_Name", models.CharField(max_length=70)),
                ("Contact_Number", models.CharField(max_length=70)),
                ("Address", models.CharField(max_length=70)),
                ("Course", models.CharField(max_length=70)),
                ("Timing", models.CharField(max_length=70)),
                ("Days", models.CharField(max_length=70)),
            ],
        ),
    ]