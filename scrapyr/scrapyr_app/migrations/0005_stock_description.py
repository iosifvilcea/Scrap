# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapyr_app', '0004_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='description',
            field=models.CharField(default=0, max_length=20000),
        ),
    ]
