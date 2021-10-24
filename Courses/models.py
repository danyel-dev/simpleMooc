from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from django.conf import settings

from django.utils import timezone


class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name_course__icontains = query) | 
            models.Q(description_course__icontains = query)
        )


class Course(models.Model):
    name_course = models.CharField(max_length=50, verbose_name='Nome do curso')
    
    slug_course = models.SlugField(verbose_name='Atalho', blank=True)
    
    description_course = models.CharField(max_length=255, verbose_name='Descrição do curso')
    
    about_course = models.TextField(verbose_name='Sobre o curso')
    
    image_course = models.ImageField(upload_to='course_img/%Y/%m/%d', verbose_name='Imagem', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add= True, verbose_name='Data de criação')
    
    update_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    objects = CourseManager()
    

    def __str__(self):
        return self.name_course


    def save(self, *args, **kargs):
        self.slug_course = slugify(self.name_course, allow_unicode=False)
        super().save(*args, **kargs)


    def get_absolute_url(self):
        return reverse('detail-course', args=[self.slug_course])


    def release_lessons(self):
        today = timezone.now().date()
        return self.Lessons.filter(release_data__lte=today)


    def course_adverts_url(self):
        return reverse('course-adverts', args=[self.slug_course])


    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
    

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso', related_name='Lessons')

    name = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    release_data = models.DateField('Data de liberação', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')


    def __str__(self):
        return self.name
    

    def is_available(self):
        if self.release_data:
            today = timezone.now().date()
            return self.release_data >= today
        return False


    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'


class Material(models.Model):
    
    name = models.CharField('Nome', max_length=100)
    embedded = models.TextField('Video embutido', blank=True)
    file = models.FileField('Arquivo', upload_to='lessons/materials', blank=True, null=True)

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)


    def is_embedded(self):
        return bool(self.embedded)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'


class subscribe(models.Model):
    STATUS_CHOICES = (
        (0, 'Análise'),
        (1, 'Aprovado'),
        (2, 'Cancelado'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuário')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, blank=True, verbose_name='Situação')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')


    def active(self):
        self.status = 1
        self.save()


    def is_approved(self):
        return self.status == 1


    def __str__(self):
        return str(self.user)


    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('user', 'course'),)


class Advert(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso', related_name='Adverts')
    title = models.CharField(max_length=100, verbose_name='Título do anúncio')
    content = models.TextField(verbose_name='Conteúdo')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Anúncio'
        verbose_name_plural = 'Anúncios'


class Comment(models.Model):
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, verbose_name='Anúncio', related_name='Comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='usuário')
    comment = models.TextField(verbose_name='Comentário')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')


    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
