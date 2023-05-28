# Generated by Django 4.2 on 2023-05-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_program_exercises'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default=None, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=None, max_length=255, unique=True, verbose_name='Email адрес'),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=None, max_length=255, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='Группы, к которым принадлежит пользователь.', related_name='myuser_set', related_query_name='myuser', to='auth.group', verbose_name='Группы'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активирован'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=None, max_length=255, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='default_password', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='', upload_to='users/photos', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='user',
            name='programs',
            field=models.ManyToManyField(to='program.program'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Доступы пользователя.', related_name='myuser_set', related_query_name='myuser', to='auth.permission', verbose_name='Доступы'),
        ),
    ]
