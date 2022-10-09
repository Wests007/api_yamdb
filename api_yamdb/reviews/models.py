from django.contrib.auth.models import AbstractUser
from django.db import models

ADMIN = 'admin'
MODERATOR = 'moderator'
USER = 'user'
ROLES_CHOICES = [
    (ADMIN, ADMIN),
    (MODERATOR, MODERATOR),
    (USER, USER)

]


class User(AbstractUser):
    username = models.CharField(max_length=150,
                                unique=True,
                                blank=False,
                                null=False,)
    # тут не забыть сделать валидатор
    email = models.EmailField(max_length=254,
                              unique=True,
                              blank=False,
                              null=False)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(max_length=9, choices=ROLES_CHOICES, default=USER)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
