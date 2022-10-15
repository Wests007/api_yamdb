# Generated by Django 2.2.16 on 2022-10-12 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20221009_2103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genretitle',
            options={'verbose_name': 'Жанры произведения', 'verbose_name_plural': 'Жанры произведений'},
        ),
        migrations.AddField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='UNKNOWN', max_length=255, null=True, verbose_name='код подтверждения'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='год'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
