from django.db import models
from django.core.validators import MaxValueValidator
from exercise.models import Exercise

# Create your models here.
class Program(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(verbose_name='Фото', upload_to='Programs/photo')
    photo_thumbnail = models.ImageField(verbose_name='Миниатюра', upload_to='Programs/photo_thumbnails')
    target = models.CharField(verbose_name='Цель', max_length=255)
    body_type = models.CharField(verbose_name='Телосложение', max_length=255)
    complexity = models.CharField(verbose_name='Сложность', max_length=255)
    training_time = models.IntegerField(verbose_name='Время тренировки', validators=[
        MaxValueValidator(255)
    ])
    trainings_per_week = models.IntegerField(verbose_name='Тренировок в неделю', validators=[
        MaxValueValidator(7)
    ])
    exercises = models.ManyToManyField( verbose_name='Упражнения', to=Exercise, related_name='programs')
    training_place = models.CharField(verbose_name='Место тренировок', max_length=255)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'