# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 01:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_aluno_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='data_nascimento',
        ),
    ]
