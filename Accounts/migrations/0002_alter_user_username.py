# Generated by Django 3.2.7 on 2021-10-16 13:54

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'O nome de usuário só pode conter letras números, ou os seguintes caracteres: @/./+/-/_', 'invalid')], verbose_name='Nome de usuário'),
        ),
    ]
