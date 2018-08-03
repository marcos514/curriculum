# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('carrera', models.CharField(max_length=200)),
                ('lugar', models.CharField(max_length=200)),
                ('sede', models.CharField(max_length=200)),
                ('comienzo', models.CharField(max_length=200)),
                ('fin', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('trabajo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('lugar', models.CharField(max_length=200)),
                ('comienzo', models.CharField(max_length=200)),
                ('fin', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lenguajes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
    ]
