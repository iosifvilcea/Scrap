from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from scrapyr_app.models import Account, CustomUser, Stock 
# from django.template.context import RequestContext


def index(request):
    #return HttpResponse("Hello, world. You're at the scrapyr index.")
    return render(request, 'scrapyr_app/index.html')

def login(request):
    request.user.email = 'fake@fake.com'
    context = RequestContext(request, {'request': request, 'user': request.user, 'type': request.user.__class__.__name__, 'email': request.user.email})
    return render_to_response('scrapyr_app/login.html', context_instance=context)
    #return render(request, 'scrapyr_app/login.html')
      
      
@login_required(login_url='/')
def home(request):
    user_objects = Account.objects.all()
    if user_objects.count() == 0:
        user_objects = "WOW"
    #account = Account.objects.get(user.username = request.user.username)
    context = RequestContext(request, {'user_objects': user_objects})
    return render_to_response('scrapyr_app/home.html', context)
            
            
def logout(request):
    auth_logout(request)
    return redirect('/')

