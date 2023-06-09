# Generated by Django 4.2 on 2023-05-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exercise", "0001_initial"),
        ("program", "0002_program_created_at_program_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="program",
            name="exercises",
            field=models.ManyToManyField(
                related_name="programs",
                to="exercise.exercise",
                verbose_name="Упражнения",
            ),
        ),
    ]
