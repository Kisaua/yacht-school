# Generated by Django 3.2.4 on 2021-07-03 06:28

from django.db import migrations, models
import yacht01.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите Ваше имя', max_length=50, verbose_name='Name')),
                ('user_email', models.EmailField(help_text='Ваш Email', max_length=70, validators=[yacht01.models.check_email_address_validity], verbose_name='Email')),
                ('subject', models.CharField(help_text='Тема сообщения', max_length=250, verbose_name='Subject')),
                ('message', models.TextField(help_text='Введите текст сообщения до 1000 символов', max_length=1000, verbose_name='Message')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
