# Generated by Django 3.2.7 on 2021-11-06 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20211105_1050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-updated_at'], 'verbose_name': 'Tópico', 'verbose_name_plural': 'Tópicos'},
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='update_at',
        ),
        migrations.AddField(
            model_name='topic',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
