from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request,'mainpage/mainpage.html')


def about(request):
    return render(request, "mainpage/about.html")

def contacts(request):
    return render(request, "mainpage/contacts.html")
