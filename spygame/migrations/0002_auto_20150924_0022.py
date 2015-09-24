# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spygame', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='team_id',
        ),
        migrations.AddField(
            model_name='team',
            name='game_id',
            field=models.ForeignKey(default='', to='spygame.Game'),
        ),
        migrations.AlterField(
            model_name='game',
            name='turn_status',
            field=models.CharField(max_length=30, default=''),
        ),
        migrations.AlterField(
            model_name='game',
            name='winner',
            field=models.CharField(max_length=30, default=''),
        ),
        migrations.AlterField(
            model_name='team',
            name='color',
            field=models.CharField(max_length=30, default=''),
        ),
    ]
