from django.db import models

class User(models.Model):
    username = models.CharField(required, min_length = 3, max_length = 20, unique = True)
    email = models.EmailField(required)
    name = madels.CharField()
    profile_pic = models.ImageField()
    member_since = models.DateTimeField('Member Since:')
    
class Stock(models.Model):
    user = models.ManyToManyField(User)
    ticker = models.CharField()
    average_daily_volume = models.BigIntegerField()
    book_value = models.DecimalField(max_digits=12, decimal_places=2)
    change = models.DecimalField(max_digits=12, decimal_places=2)
    dividend_per_share = models.DecimalField(max_digits=12, decimal_places=2)
    dividend_yield = models.DecimalField(max_digits=12, decimal_places=2)
    earnings_per_share = models.DecimalField(max_digits=12, decimal_places=2)
    ebitda = models.DecimalField(max_digits=12, decimal_places=2)
    fifty_day_moving_avg = models.DecimalField(max_digits=12, decimal_places=2)
    fifty_two_week_high = models.DecimalField(max_digits=12, decimal_places=2)
    fifty_two_week_low = models.DecimalField(max_digits=12, decimal_places=2)
    market_cap = models.CharField(max_digits=12, decimal_places=2)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    price_book_ratio = models.DecimalField(max_digits=2, decimal_places=2)
    price_earnings_growth_ratio = models.DecimalField(max_digits=2, decimal_places=2)
    price_earnings_ratio = models.DecimalField(max_digits=2, decimal_places=2)
    price_sales_ratio = models.DecimalField(max_digits=12, decimal_places=2)
    short_ratio = models.DecimalField(max_digits=2, decimal_places=2)
    stock_exchange = models.CharField()
    two_hundred_day_moving_avg =  = models.DecimalField(max_digits=12, decimal_places=2)
    volume = BigIntegerField(default = 0)
    
class Article(models.Model):
    title = models.CharField(max_length = 80)
    author = models.CharField(max_length = 40)
    pub_date = models.DateTimeField()
    content = models.TextField()
    stock = models.ManyToManyField(Stock) 
