# Generated by Django 4.2 on 2023-05-30 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("program", "0003_program_exercises"),
        ("authentication", "0012_merge_20230530_2014"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="programs",
            field=models.ManyToManyField(
                blank=True,
                default=[],
                related_name="programs",
                to="program.program",
                verbose_name="Программы",
            ),
        ),
    ]
