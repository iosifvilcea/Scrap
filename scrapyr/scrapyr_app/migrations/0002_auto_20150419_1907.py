# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapyr_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='ebitda',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
