# Generated by Django 4.2.7 on 2023-11-26 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Наименование операции')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание операции')),
                ('cost', models.FloatField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Операция',
                'verbose_name_plural': 'Операции',
            },
        ),
    ]
