# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 21:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170719_2054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='codigo_geral',
            new_name='codigo',
        ),
    ]