# Generated by Django 3.2.7 on 2021-10-05 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0004_auto_20211005_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image_course',
            field=models.ImageField(blank=True, null=True, upload_to='course_img/%Y/%m/%d', verbose_name='Imagem'),
        ),
    ]
