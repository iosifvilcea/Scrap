from django.contrib import admin
from scrapyr_app.models import Account, Stock, Portfolio, CustomUser, Article, Library

class StockInline(admin.TabularInline):
      model = Portfolio
      extra = 3

class ArticleInline(admin.TabularInline):
      model = Library
      extra = 3 

class StockAdmin(admin.ModelAdmin):
      inlines = [StockInline]
      
class ArticleAdmin(admin.ModelAdmin):
      inlines = [ArticleInline]

class AccountAdmin(admin.ModelAdmin):
      fieldsets = [
        ('Username',               {'fields': ['user']}),
      ]      
      inlines = [StockInline, ArticleInline]

class UserAdmin(admin.ModelAdmin):
      model = CustomUser

admin.site.register(Stock, StockAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Article, ArticleAdmin)
