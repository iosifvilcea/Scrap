from django.shortcuts import render

from django.http import HttpResponse


def index(request):
      #return HttpResponse("Hello, world. You're at the scrapyr index.")
      return render(request, 'scrapyr_app/index.html')

# Create your views here.
