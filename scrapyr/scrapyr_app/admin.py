from django.contrib import admin
from scrapyr_app.models import Account, Stock, Portfolio, CustomUser

class PortfolioInline(admin.TabularInline):
      model = Portfolio
      extra = 1

class StockAdmin(admin.ModelAdmin):
      inlines = (PortfolioInline,)
      
class AccountAdmin(admin.ModelAdmin):
      inlines = (PortfolioInline,)

class UserAdmin(admin.ModelAdmin):
      model = CustomUser

admin.site.register(Stock, StockAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(CustomUser, UserAdmin)
