# Generated by Django 4.2 on 2023-05-31 09:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("program", "0003_program_exercises"),
        ("authentication", "0013_alter_user_programs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="programs",
            field=models.ManyToManyField(
                blank=True,
                default=[],
                null=True,
                related_name="programs",
                to="program.program",
                verbose_name="Программы",
            ),
        ),
    ]