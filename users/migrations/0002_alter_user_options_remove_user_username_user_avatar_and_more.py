# Generated by Django 5.0.4 on 2024-04-10 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, help_text='Загрузите фото', null=True, upload_to='users/avatar', verbose_name='Аватар'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, help_text='Укажите город', max_length=100, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, help_text='Укажите номер телефона', max_length=35, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Укажите почту', max_length=50, unique=True, verbose_name='Email'),
        ),
    ]