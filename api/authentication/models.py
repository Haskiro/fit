from django.db import models

# from django.contrib.auth.models import Group
from django.utils import timezone
from program.models import Program

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(
        verbose_name="Имя пользователя", max_length=255, unique=True, default=None
    )

    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=40, null=True)
    photo = models.ImageField(
        verbose_name="Фото", upload_to="users/photos", default="", blank=True
    )
    birthdate = models.DateField(
        verbose_name="Дата рождения", null=True, default=None, blank=True
    )
    # programs = models.ManyToManyField(Program, blank=True)
    programs = models.ManyToManyField(
        verbose_name="Программы",
        to=Program,
        related_name="programs",
        blank=True,
        default=[],
    )

    is_active = models.BooleanField(verbose_name="Активирован", default=True)
    is_superuser = models.BooleanField(verbose_name="Администратор", default=False)
    is_staff = models.BooleanField(verbose_name="Работник", default=True)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
