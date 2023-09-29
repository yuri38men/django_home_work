# Generated by Django 4.2.4 on 2023-09-29 20:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=250, verbose_name='слаг')),
                ('content', models.TextField(verbose_name='содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs/', verbose_name='изображение')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='признак публикации')),
                ('views_count', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
