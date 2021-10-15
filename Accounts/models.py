from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=50, verbose_name='Nome de usuário', unique=True)
    email = models.EmailField(unique=True, verbose_name='E-mail')
    full_name = models.CharField(max_length=100, blank=True, verbose_name='Nome completo')
    is_active = models.BooleanField(blank=True, default=True, verbose_name='Está ativo?')
    is_staff = models.BooleanField(blank=True, default=False, verbose_name='Pertence a equipe?')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Data de entrada')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name']


    def __str__(self):
        return self.full_name or self.username


    def get_short_name(self):
        return self.username


    def get_full_name(self):
        return str(self)


    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
