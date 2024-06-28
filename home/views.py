from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def trainingcourses(request):
    return render(request, 'trainingcourses.html')

def consultancy(request):
    return render(request, 'consultancy.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')