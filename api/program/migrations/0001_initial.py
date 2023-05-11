# Generated by Django 4.2 on 2023-05-10 11:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='Programs/photo', verbose_name='Фото')),
                ('photo_thumbnail', models.ImageField(upload_to='Programs/photo_thumbnails', verbose_name='Миниатюра')),
                ('target', models.CharField(max_length=255, verbose_name='Цель')),
                ('body_type', models.CharField(max_length=255, verbose_name='Телосложение')),
                ('complexity', models.CharField(max_length=255, verbose_name='Сложность')),
                ('training_time', models.IntegerField(validators=[django.core.validators.MaxValueValidator(255)], verbose_name='Время тренировки')),
                ('trainings_per_week', models.IntegerField(validators=[django.core.validators.MaxValueValidator(7)], verbose_name='Тренировок в неделю')),
                ('training_place', models.CharField(max_length=255, verbose_name='Место тренировок')),
            ],
            options={
                'verbose_name': 'Программа',
                'verbose_name_plural': 'Программы',
            },
        ),
    ]
