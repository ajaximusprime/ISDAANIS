from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def  index(request):
    return HttpResponse('<h1>my first app</h1>')

def  isforms(request):
    return render(request, 'MCforms.html' )

def  isdashboard(request):
    return render(request, 'dashboard.html' )

def  isadmindashboard(request):
    return render(request, 'admindash.html' )