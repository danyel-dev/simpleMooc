# Generated by Django 3.2.7 on 2021-11-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_alter_topic_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='identificador'),
        ),
    ]
