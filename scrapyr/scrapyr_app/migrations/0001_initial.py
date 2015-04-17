# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('author', models.CharField(max_length=40)),
                ('pub_date', models.DateTimeField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=18)),
                ('last_name', models.CharField(max_length=22)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('email', models.EmailField(default=b'myemail@fake.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article', models.ForeignKey(to='scrapyr_app.Article')),
                ('profile', models.ForeignKey(to='scrapyr_app.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile', models.ForeignKey(to='scrapyr_app.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticker', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=30)),
                ('last_sale', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('market_cap', models.CharField(max_length=10)),
                ('ipo_year', models.CharField(max_length=4)),
                ('sector', models.CharField(max_length=30)),
                ('industry', models.CharField(max_length=30)),
                ('summary_quote', models.URLField()),
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
            model_name='portfolio',
            name='stock',
            field=models.ForeignKey(to='scrapyr_app.Stock'),
        ),
        migrations.AddField(
            model_name='article',
            name='stocks',
            field=models.ManyToManyField(to='scrapyr_app.Stock'),
        ),
        migrations.AddField(
            model_name='account',
            name='articles',
            field=models.ManyToManyField(to='scrapyr_app.Article', through='scrapyr_app.Library'),
        ),
        migrations.AddField(
            model_name='account',
            name='stocks',
            field=models.ManyToManyField(to='scrapyr_app.Stock', through='scrapyr_app.Portfolio'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(to='scrapyr_app.CustomUser'),
        ),
    ]
