# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 18:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_disciplinas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Disciplinas',
            new_name='Disciplina',
        ),
    ]