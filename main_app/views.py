from django.shortcuts import render
from django.http import HttpResponse # to send simple HTTP responses
from .models import Car  # Import the Car model 

# Create your views here.
def home(request):
    return render(request, 'home.html')
    


def about(request):
    return render(request, 'about.html')






def gallery(request):
    cars = Car.objects.all()  # Fetch all car records from the database
    return render(request, 'cars/gallery.html', {'cars': cars})