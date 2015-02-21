from django.db import models

class User(models.Model):
    username = models.CharField()
    email = models.EmailField()
    name = models.CharField()
    profile_pic = models.ImageField()
    member_since = models.DateTimeField()
    
class Stock(models.Model):
    user = models.ManyToManyField(User)
    ticker = models.CharField()
    average_daily_volume = models.BigIntegerField()
    book_value = models.DecimalField()
    change = models.DecimalField()
    dividend_per_share = models.DecimalField()
    dividend_yield = models.DecimalField()
    earnings_per_share = models.DecimalField()
    ebitda = models.DecimalField()
    fifty_day_moving_avg = models.DecimalField()
    fifty_two_week_high = models.DecimalField()
    fifty_two_week_low = models.DecimalField()
    market_cap = models.CharField()
    price = models.DecimalField()
    price_book_ratio = models.DecimalField()
    price_earnings_growth_ratio = models.DecimalField()
    price_earnings_ratio = models.DecimalField()
    price_sales_ratio = models.DecimalField()
    short_ratio = models.DecimalField()
    stock_exchange = models.CharField()
    two_hundred_day_moving_avg = models.DecimalField()
    volume = models.BigIntegerField(default = 0)
    
class Article(models.Model):
    title = models.CharField(max_length = 80)
    author = models.CharField(max_length = 40)
    pub_date = models.DateTimeField()
    content = models.TextField()
    stock = models.ManyToManyField(Stock) 
