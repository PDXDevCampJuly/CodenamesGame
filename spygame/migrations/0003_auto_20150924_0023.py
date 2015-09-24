# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spygame', '0002_auto_20150924_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='turn_status',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='game',
            name='winner',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='team',
            name='color',
            field=models.CharField(max_length=30),
        ),
    ]
