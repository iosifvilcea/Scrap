from django.contrib import admin
from scrapyr_app.models import Profile, Stock, Portfolio

class PortfolioInline(admin.TabularInline):
      model = Portfolio
      extra = 1

class StockAdmin(admin.ModelAdmin):
      inlines = (PortfolioInline,)
      
class ProfileAdmin(admin.ModelAdmin):
      inlines = (PortfolioInline,)


admin.site.register(Stock, StockAdmin)
admin.site.register(Profile, ProfileAdmin)
