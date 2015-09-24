# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def build_dictionary(apps, schema_editor):
    """Populate spygame_dictionary table with words from list_of_nouns.txt."""
    Dictionary = apps.get_model("spygame", "Dictionary")

    # Open and read line-by-line from list_of_nouns.txt
    with open('docs/list_of_nouns.txt', 'r') as f:
        for line in f:
            noun = line.strip()
            if noun[0] == "#":
                continue
            word = Dictionary(word=noun)
            word.save()


def clear_dictionary(apps, schema_editor):
    """Delete all rows of the dictionary table."""
    Dictionary = apps.get_model("spygame", "Dictionary")
    Dictionary.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('spygame', '0003_auto_20150924_0023'),
    ]

    operations = [
        migrations.RunPython(build_dictionary, clear_dictionary),
    ]
