from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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



def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)  # Fetch the car with the given ID
    return render(request, 'cars/car-detail.html', {'car': car})



class CarCreate(CreateView):
    model = Car
    fields = '__all__'


class CarUpdate(UpdateView):
    model = Car
    fields = ['color', 'description', 'price']



class CarDelete(DeleteView):
    model = Car
    success_url = '/gallery/'
    
    