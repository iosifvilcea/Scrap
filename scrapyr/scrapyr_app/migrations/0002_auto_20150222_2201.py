# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scrapyr_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='stocks',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='profile',
            field=models.ForeignKey(to='scrapyr_app.Account'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='account',
            name='stocks',
            field=models.ManyToManyField(to='scrapyr_app.Stock', through='scrapyr_app.Portfolio'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(related_name='profile', verbose_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
