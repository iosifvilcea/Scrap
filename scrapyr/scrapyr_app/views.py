from django.db import models
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from scrapyr_app.models import Account, CustomUser, Stock 
from django.shortcuts import redirect
from scrapyr_app.forms import CustomUserForm
from django.core.context_processors import csrf
from yahoo_finance import Share
import ystockquote 
#from scrapyr_app.static import stocks
#from scrapyr_app.forms import ProfileUpdateForm

def stocks(request):
    stocks = Stock.objects.all()
    context = RequestContext(request, {'request': request, 'stocks':stocks})
    return render_to_response('scrapyr_app/stocks.html', context=context)

# View for Single stock login not required 
# If no stock is requested sent them to our 
# awesome list of stocks

def view_stock(request, ticker):
    stock = get_object_or_404(Stock, ticker=ticker)
    return render_to_response("scrapyr_app/stock.html", dict(stock=stock))

def view_article(request, ticker):
    article = get_object_or_404(Article, ticker=ticker)
    return render_to_response("scrapyr_app/article.html", dict(article=article))

def stock(request):
    if request.method == 'POST':
        companyName=request.POST['ticker']
        companyName = companyName.upper()
        stock = Stock.objects.get(ticker=companyName)
        ystock = Share(companyName)
        stock.book_value = ystockquote.get_book_value(companyName)  
        stock.change = ystockquote.get_change(companyName) 
        stock.dividend_per_share = ystockquote.get_dividend_per_share(companyName) 
        stock.dividend_yield = ystockquote.get_dividend_yield(companyName) 
        stock.ebitda = ystockquote.get_ebitda(companyName) 
        stock.fifty_two_week_high = ystockquote.get_52_week_high(companyName) 
        stock.fifty_two_week_low = ystockquote.get_52_week_low(companyName) 
        stock.market_cap = ystockquote.get_market_cap(companyName) 
        stock.short_ratio = ystockquote.get_short_ratio(companyName) 
        stock.stock_exchange = ystockquote.get_stock_exchange(companyName) 
        stock.volume = ystockquote.get_volume(companyName)
        stock.price = ystockquote.get_price(companyName)
        #yahoo_finance
        stock.average_daily_volume = ystock.get_avg_daily_volume()
        stock.earnings_per_share = ystock.get_price_earnings_ratio()
        stock.fifty_day_moving_avg = ystock.get_50day_moving_avg()
        stock.two_hundred_day_moving_avg =  ystock.get_200day_moving_avg()
        stock.price_book_ratio = ystock.get_price_book()
        stock.last_sale = ystock.get_price()
        stock.price_earnings_growth_ratio = ystock.get_price_earnings_growth_ratio()
        stock.price_earnings_ratio = ystock.get_price_earnings_ratio()
        stock.price_sales_ratio = ystock.get_price_sales()
        stock.save()

        context = RequestContext(request, {'request': request, 'stock':stock})
    return render_to_response('scrapyr_app/stock.html', context=context)
          
def index(request):
    #return HttpResponse("Hello, world. You're at the scrapyr index.")
    return render(request, 'scrapyr_app/index.html')

# login page redirects to profile if logged in
# need to change case for anonymous user to redirect 
# to homepage 
def login(request):
    if request.user.__class__.__name__ is 'AnonymousUser':
        message = "You are anonymous"
        context = RequestContext(request, {'request': request, 'user': request.user, 'type': request.user.__class__.__name__, 'message': message})
    elif request.user.__class__.__name__ is 'CustomUser':
        loggedInUser = request.user
        return redirect('scrapyr_app.views.profile')
    else:
        message = 'already have an email!'
        context = RequestContext(request, {'request': request, 'user': request.user, 'type': request.user.__class__.__name__, 'message': message})
    return render_to_response('scrapyr_app/login.html', context=context)
    #return render(request, 'scrapyr_app/login.html')
      

# dashboard is currently not a functioning view
@login_required(login_url='/')
def dashboard(request):
    context = RequestContext(request, {'user_objects': user_objects})
    return render_to_response('scrapyr_app/home.html', context)
    
# Profile Page for user considering making an edit 
# profile/settings page eventually
#def profile(request):
#    return render(request, 'scrapyr_app/profile.html')

##############################################################################

def profile(request):
    if request.user.__class__.__name__ is 'CustomUser':
        c_user = get_object_or_404(CustomUser, pk= request.user.pk)
    else:
        return render_to_response('scrapyr_app/login.html')
    try:
        account = Account.objects.get(user=c_user)
    except:
        account = Account(user=c_user)
        account.save()
        
    return render(request, 'scrapyr_app/profile.html')
 
def edit_profile(request):
    if request.user.__class__.__name__ is 'CustomUser':
        c_user = get_object_or_404(CustomUser, pk= request.user.pk)
    else:
        return render_to_response('scrapyr_app/login.html')
        
    if request.POST:
        form = CustomUserForm(request.POST, instance=c_user)
        if form.is_valid():
            c_user = form.save(commit=False)
            c_user.save()
            #return redirect('scrapyr_app/edit_profile.html', user=request.user)
    form = CustomUserForm(instance=c_user)
    return render(request, 'scrapyr_app/edit_profile.html', {'form': form})

############################################################################## 
def logout(request):
    auth_logout(request)
    return redirect('/')
