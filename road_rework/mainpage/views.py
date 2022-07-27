from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    return render(request,'mainpage/mainpage.html')

def repair(request):
    return render(request, "mainpage/repair.html")

def looks(request):
    return render(request, "mainpage/looks.html")

def tech(request):
    return render(request, "mainpage/tech.html")
