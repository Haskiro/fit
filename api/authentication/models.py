from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import Group
from django.utils import timezone
from program.models import Program

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email адрес' ,max_length=255, unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    photo = models.ImageField(verbose_name='Фото', upload_to='users/photos', default="")
    birthdate = models.DateField(verbose_name='Дата рождения', null=True, default=None)
    programs = models.ManyToManyField(Program)


    is_active = models.BooleanField(verbose_name='Активирован', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['first_name', 'last_name']

     # Добавляем параметр related_name
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='Группы',
        blank=True,
        help_text='Группы, к которым принадлежит пользователь.',
        related_name='myuser_set',
        related_query_name='myuser',
    )
    # Добавляем параметр related_name
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='Доступы',
        blank=True,
        help_text='Доступы пользователя.',
        related_name='myuser_set',
        related_query_name='myuser',
    )


    def __str__(self):
        return self.email

    class Meta: 
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

