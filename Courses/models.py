from django.db import models


class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name_course__icontains = query) | 
            models.Q(description_course__icontains = query)
        )


class Course(models.Model):
    name_course = models.CharField(max_length=100, verbose_name='Nome do curso')
    
    slug_course = models.SlugField(verbose_name='Atalho')
    
    description_course = models.TextField(verbose_name='Descrição do curso')
    
    image_course = models.ImageField(upload_to='course_img/%Y/%m/%d', verbose_name='Imagem', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add= True, verbose_name='Data de criação')
    
    update_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    objects = CourseManager()
    

    def __str__(self):
        return self.name_course


    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
    