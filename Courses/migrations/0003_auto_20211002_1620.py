# Generated by Django 3.2.7 on 2021-10-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_auto_20211002_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
        migrations.AlterField(
            model_name='course',
            name='description_course',
            field=models.TextField(verbose_name='Descrição do curso'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image_course',
            field=models.ImageField(default=1, upload_to='course_img/%Y/%m/%d', verbose_name='Imagem'),
            preserve_default=False,
        ),
    ]
