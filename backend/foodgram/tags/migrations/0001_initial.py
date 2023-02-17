# Generated by Django 2.2.19 on 2023-02-17 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название тега', max_length=200, verbose_name='Название тега')),
                ('color', models.CharField(help_text='Цвет тега', max_length=7, verbose_name='Цвет тега')),
                ('slug', models.SlugField(help_text='Идентификатор тега', unique=True, verbose_name='Идентификатор тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
    ]
