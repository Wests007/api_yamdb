from django.contrib.auth.models import AbstractUser
from django.db import models

ROLES_CHOICES = [
    ('ADMIN', 'admin'),
    ('MODERATOR', 'moderator'),
    ('USER', 'user')

]


class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(max_length=9, choices=ROLES_CHOICES, default='user')

