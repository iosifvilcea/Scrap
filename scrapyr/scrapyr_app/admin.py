from django.contrib import admin
from scrapyr_app.models import Account, Stock, Portfolio
from django.contrib.auth.models import User
class PortfolioInline(admin.TabularInline):
      model = Portfolio
      extra = 1

class StockAdmin(admin.ModelAdmin):
      inlines = (PortfolioInline,)
      
class AccountAdmin(admin.ModelAdmin):
      inlines = (PortfolioInline,)


admin.site.register(Stock, StockAdmin)
admin.site.register(Account, AccountAdmin)
