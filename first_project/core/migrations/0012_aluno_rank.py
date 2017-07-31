# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_aluno_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='rank',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
    ]
