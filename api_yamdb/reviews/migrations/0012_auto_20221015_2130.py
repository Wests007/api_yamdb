# Generated by Django 2.2.16 on 2022-10-15 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_auto_20221015_2119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('id',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('id',), 'verbose_name': 'Комментарий на отзыв', 'verbose_name_plural': 'Комментарии на отзывы'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('id',), 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='genretitle',
            options={'ordering': ('id',), 'verbose_name': 'Жанры произведения', 'verbose_name_plural': 'Жанры произведений'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('id',), 'verbose_name': 'Отзыв на произведение', 'verbose_name_plural': 'Отзывы на произведения'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('id',), 'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]