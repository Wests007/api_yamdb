from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

ADMIN = 'admin'
MODERATOR = 'moderator'
USER = 'user'
ROLES_CHOICES = [
    (ADMIN, ADMIN),
    (MODERATOR, MODERATOR),
    (USER, USER)

]


class User(AbstractUser):
    username = models.CharField(max_length=50,
                                unique=True,
                                blank=False,
                                null=False)
    # тут не забыть сделать валидатор
    email = models.EmailField(unique=True,
                              blank=False,
                              null=False)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
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


class Genre(models.Model):
    name = models.TextField('Название',
                            blank=False,
                            max_length=150)
    slug = models.SlugField('Slug',
                            blank=False,
                            unique=True,
                            db_index=True)

    def __str__(self):
        return self.name[0:10]


class Category(models.Model):
    name = models.TextField(
        'Название',
        blank=False,
        max_length=150
    )
    slug = models.SlugField(
        'slug',
        blank=False,
        unique=True,
        db_index=True
    )

    def __str__(self):
        return self.name[0:10]


class Title(models.Model):
    name = models.TextField(
        'Название',
        blank=False,
        max_length=200,
        db_index=True
    )
    year = models.IntegerField('год', blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name='Категория'
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        db_index=True,
        related_name='titles',
        verbose_name='Жанр'
    )
    description = models.CharField(
        'Описание',
        max_length=200,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name[0:10]


class Review(models.Model):
    text = models.TextField(
        'Текст отзыва',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.PositiveSmallIntegerField(
        'Оценка произведения',
        db_index=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )


class Comment(models.Model):
    text = models.TextField(
        'Текст комментария',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )
