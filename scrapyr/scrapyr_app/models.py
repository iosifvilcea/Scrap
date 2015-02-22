from django.db import models
from django.db import models
from awesome_avatar.fields import AvatarField
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaLanguageBaseProfile


class Stock(models.Model):
      ticker = models.CharField(max_length=5)
      average_daily_volume = models.BigIntegerField()
      book_value = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      change = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      dividend_per_share = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      dividend_yield = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      earnings_per_share = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      ebitda = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      fifty_day_moving_avg = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      fifty_two_week_high = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      fifty_two_week_low = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      market_cap = models.CharField(max_length=10)
      price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      price_book_ratio = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      price_earnings_growth_ratio = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      price_earnings_ratio = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      price_sales_ratio = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      short_ratio = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      stock_exchange = models.CharField(max_length=7)
      two_hundred_day_moving_avg = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      volume = models.BigIntegerField(default=0)

'''
class Article(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=40)
    pub_date = models.DateTimeField()
    content = models.TextField()
    stocks = models.ManyToManyField(Stock)
'''

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, verbose_name=_('user'), related_name='profile')
    stocks = models.ManyToManyField(Stock, through='Portfolio')

class Portfolio(models.Model):
    stock = models.ForeignKey(Stock)                                                                                                          
    profile = models.ForeignKey(Profile)
# Create your models here.
