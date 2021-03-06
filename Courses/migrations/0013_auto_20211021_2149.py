# Generated by Django 3.2.7 on 2021-10-22 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0012_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('release_data', models.DateField(blank=True, null=True, verbose_name='Data de liberação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Lessons', to='Courses.course', verbose_name='Curso')),
            ],
            options={
                'verbose_name': 'Aula',
                'verbose_name_plural': 'Aulas',
            },
        ),
        migrations.AlterField(
            model_name='advert',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Adverts', to='Courses.course', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='advert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='Courses.advert', verbose_name='Anúncio'),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('embedded', models.TextField(blank=True, verbose_name='Video embutido')),
                ('file', models.FileField(blank=True, null=True, upload_to='lessons/materials', verbose_name='Arquivo')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.lesson')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materials',
            },
        ),
    ]
