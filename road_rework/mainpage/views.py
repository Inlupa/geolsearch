from django.shortcuts import render

def homepage(request):
    return render(request,'mainpage/mainpage.html')

def repair(request):
    return render(request, "mainpage/repeir.html")

def looks(request):
    return render(request, "mainpage/looks.html")

def tech(request):
    return render(request, "mainpage/tech.html")
