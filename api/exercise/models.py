from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class Exercise(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    approaches = models.TextField(verbose_name="Подходы")
    photo = models.ImageField(verbose_name="Фото", upload_to="Exercises/photo")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Упражнение"
        verbose_name_plural = "Упражнения"
