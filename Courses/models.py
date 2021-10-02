from django.db import models


class Course(models.Model):
    name_course = models.CharField(max_length=100, verbose_name='Nome do curso')
    
    slug_course = models.SlugField(verbose_name='Atalho')
    
    description_course = models.TextField(verbose_name='Descrição do curso')
    
    image_course = models.ImageField(upload_to='course_img/%Y/%m/%d', verbose_name='Imagem')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    
    update_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
