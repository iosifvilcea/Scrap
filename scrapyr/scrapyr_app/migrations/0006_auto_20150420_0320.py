# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapyr_app', '0005_stock_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='ebitda',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
