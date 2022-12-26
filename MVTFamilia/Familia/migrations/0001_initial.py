# Generated by Django 4.1.4 on 2022-12-26 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Persona",
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
                ("tipo", models.CharField(max_length=20)),
                ("nombre", models.CharField(max_length=100)),
                ("edad", models.IntegerField()),
                ("sexoM", models.BooleanField()),
                ("actividad", models.CharField(max_length=100)),
                ("imagen", models.CharField(max_length=200)),
            ],
        ),
    ]
