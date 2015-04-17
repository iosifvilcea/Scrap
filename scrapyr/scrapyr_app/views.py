from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from scrapyr_app.models import Account, CustomUser, Stock 
from django.shortcuts import redirect
from scrapyr_app.forms import CustomUserForm
#from scrapyr_app.static import stocks
#from scrapyr_app.forms import ProfileUpdateForm

def stocks(request):
    stocks = Stock.objects.all()
    context = RequestContext(request, {'request': request, 'stocks':stocks})
    return render_to_response('scrapyr_app/stocks.html', context=context)


# View for Single stock login not required 
# If no stock is requested sent them to our 
# awesome list of stocks



def stock(request):
    if request.method == 'POST':
        companyName=request.POST['ticker']
        stock = Stock.objects.get(ticker=companyName)
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

def profile(request):
    if request.user.__class__.__name__ is 'CustomUser':
        c_user = get_object_or_404(CustomUser, pk= request.user.pk)
    else:
        return render_to_response('scrapyr_app/login.html')
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=c_user)
        if form.is_valid():
            c_user = form.save(commit=False)
            c_user.username = request.user.username
            c_user.save()
            return redirect('scrapyr_app.views.index', user=request.user)
    form = CustomUserForm(instance=c_user)
    return render(request, 'scrapyr_app/profile.html', {'form': form})
 
def logout(request):
    auth_logout(request)
    return redirect('/')

