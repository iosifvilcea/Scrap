from django.db import models

class Stock(models.Model):
      def __unicode__(self):
               return 'TAG: ' + self.ticker
      ticker = models.CharField(max_length=5)
      name = models.CharField(max_length=30)
      last_sale = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      market_cap = models.CharField(max_length=10)
      ipo_year = models.CharField(max_length=4)
      sector = models.CharField(max_length = 30)
      industry = models.CharField(max_length = 30)
      summary_quote = models.URLField()
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
      price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      price_book_ratio = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      price_earnings_growth_ratio = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      price_earnings_ratio = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      price_sales_ratio = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      short_ratio = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      stock_exchange = models.CharField(max_length=7)
      two_hundred_day_moving_avg = models.DecimalField(max_digits=15, decimal_places=2, default=0)
      volume = models.BigIntegerField(default=0)


class Article(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=40)
    pub_date = models.DateTimeField()
    content = models.TextField()
    stocks = models.ManyToManyField(Stock)

class UserManager(models.Manager):
    def create_user(self, username, email):
        return self.model._default_manager.create(username=username, email=email)

                
                
class CustomUser(models.Model):
     def __unicode__(self):
              return  self.username
     username = models.CharField(max_length=128)
     first_name = models.CharField(max_length=18)
     last_name = models.CharField(max_length = 22)
     last_login = models.DateTimeField(blank=True, null=True)
     email = models.EmailField(default='myemail@fake.com')
     objects = UserManager()
     def is_active(self):
         return True
         
     def is_staff(self):
         return False
     
     def is_authenticated(self):
         return True
         
     def has_module_perms(self, app_label):
         return True
         
     def has_perm(self, app_label):
         return True

class AccountManager(models.Manager):
    def create_account(self, user):
        return self.model._default_manager.create(user=user)
    def all(self, session=None):
        return self.all()


class Account(models.Model):
    def __unicode__(self):
             return 'Account: ' + self.user.username
    user = models.OneToOneField(CustomUser, unique=True)
    stocks = models.ManyToManyField(Stock, through='Portfolio')
    objects = AccountManager()
    articles = models.ManyToManyField(Article, through='Library')

class Portfolio(models.Model):
    stock = models.ForeignKey(Stock)
    profile = models.ForeignKey(Account)

class Library(models.Model):
    article = models.ForeignKey(Article)
    profile = models.ForeignKey(Account)
# Create your models here.
