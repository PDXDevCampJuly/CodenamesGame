# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('color', models.CharField(max_length=30)),
                ('x_coord', models.IntegerField()),
                ('y_coord', models.IntegerField()),
                ('revealed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('word', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('word', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('turn_status', models.CharField(max_length=30)),
                ('winner', models.CharField(max_length=30)),
                ('password', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team_id',
            field=models.ForeignKey(to='spygame.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_id',
            field=models.ForeignKey(to='spygame.Team'),
        ),
        migrations.AddField(
            model_name='clue',
            name='game_id',
            field=models.ForeignKey(to='spygame.Game'),
        ),
        migrations.AddField(
            model_name='clue',
            name='team_id',
            field=models.ForeignKey(to='spygame.Team'),
        ),
        migrations.AddField(
            model_name='card',
            name='dict_word',
            field=models.ForeignKey(to='spygame.Dictionary'),
        ),
        migrations.AddField(
            model_name='card',
            name='game_id',
            field=models.ForeignKey(to='spygame.Game'),
        ),
    ]
