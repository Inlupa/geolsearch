from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required
def homepage(request):
    return render(request,'mainpages/homepage.html')

def wells(request):
    return render(request, 'mainpages/wells.html')

def drawwells(request):
    return render(request,'mainpages/drawwells.html')

def springs(request):
    return render(request,'mainpages/springs.html')

def VZU(request):
    return render(request,'mainpages/VZU.html')

