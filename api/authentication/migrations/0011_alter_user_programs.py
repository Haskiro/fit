# Generated by Django 4.2 on 2023-05-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("program", "0003_program_exercises"),
        ("authentication", "0010_alter_user_first_name_alter_user_last_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="programs",
            field=models.ManyToManyField(
                blank=True,
                related_name="programs",
                to="program.program",
                verbose_name="Программы",
            ),
        ),
    ]