# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeccionBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('texto', models.CharField(max_length=150)),
                ('background', models.FileField(upload_to='static/images')),
                ('logo', models.FileField(upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='SeccionClientes',
            fields=[
                ('id_usuario', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('avatar', models.FileField(upload_to='static/avatar')),
                ('nombre', models.CharField(max_length=50)),
                ('historia', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SeccionDeMedios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('logo', models.FileField(upload_to='static/medios')),
                ('texto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SeccionNoticias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('resumen', models.CharField(max_length=80)),
                ('texto', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='SeccionPatrocinantes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('logo', models.FileField(upload_to='static/patrocinantes')),
            ],
        ),
    ]
