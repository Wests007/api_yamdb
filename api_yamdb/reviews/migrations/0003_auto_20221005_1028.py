# Generated by Django 2.2.16 on 2022-10-05 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20221004_1003'),
    ]

    operations = [
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