# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos', 'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.TextField(verbose_name='Sobre o curso', blank=True),
        ),
    ]
