# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapyr_app', '0003_auto_20150419_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
