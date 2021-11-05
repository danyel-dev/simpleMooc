from django.db import models
from django.conf import settings


from taggit.managers import TaggableManager


class Topic(models.Model):

    title = models.CharField(max_length=100, verbose_name='Título')
    body = models.TextField(verbose_name='Mensagem')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Autor', related_name='topics')
    
    views = models.IntegerField(blank=True, default=0, verbose_name='Visualizações')
    answers = models.IntegerField(blank=True, default=0, verbose_name='Respostas')

    tags = TaggableManager()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Tópico'
        verbose_name_plural = 'Tópicos'
        ordering = ['-update_at']


class Reply(models.Model):
    
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Tópico', related_name='replies')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Autor', related_name='replies')

    reply = models.TextField(verbose_name='Resposta')

    corrent = models.BooleanField(blank=True, default=False, verbose_name='Correta?')

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.reply[:30]


    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'
        ordering = ['-corrent', '-created_at']
