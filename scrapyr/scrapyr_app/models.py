from django.db import models

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
class UserManager(models.Manager):
    def create_user(self, username, email):
        return self.model._default_manager.create(username=username)
                
                
class CustomUser(models.Model):
     username = models.CharField(max_length=128) 
     last_login = models.DateTimeField(blank=True, null=True)
     
     objects = UserManager()
     
     def is_authenticated(self):
         return True
    



class Account(models.Model):
    user = models.OneToOneField(CustomUser, unique=True)
    stocks = models.ManyToManyField(Stock, through='Portfolio')

class Portfolio(models.Model):
    stock = models.ForeignKey(Stock)                                                                                                          
    profile = models.ForeignKey(Account)
# Create your models here.
