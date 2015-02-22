# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticker', models.CharField(max_length=5)),
                ('average_daily_volume', models.BigIntegerField()),
                ('book_value', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('change', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('dividend_per_share', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('dividend_yield', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('earnings_per_share', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('ebitda', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('fifty_day_moving_avg', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('fifty_two_week_high', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('fifty_two_week_low', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('market_cap', models.CharField(max_length=10)),
                ('price', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('price_book_ratio', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('price_earnings_growth_ratio', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('price_earnings_ratio', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('price_sales_ratio', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('short_ratio', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('stock_exchange', models.CharField(max_length=7)),
                ('two_hundred_day_moving_avg', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('volume', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='stocks',
            field=models.ManyToManyField(to='scrapyr_app.Stock', through='scrapyr_app.Portfolio'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(related_name='profile', verbose_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='profile',
            field=models.ForeignKey(to='scrapyr_app.Profile'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='stock',
            field=models.ForeignKey(to='scrapyr_app.Stock'),
        ),
    ]
