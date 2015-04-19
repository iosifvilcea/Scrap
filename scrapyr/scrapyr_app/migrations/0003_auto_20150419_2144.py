# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapyr_app', '0002_auto_20150419_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.URLField(default=b'www.google.com', max_length=300),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ebitda',
            field=models.DecimalField(default=0, max_digits=15, decimal_places=2),
        ),
    ]
