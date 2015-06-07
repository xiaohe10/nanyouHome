from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html',locals())

def virtualPool(request):
    return render(request,'virtualPool.html',locals())