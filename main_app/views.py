from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse # to send simple HTTP responses
from .models import Car  # Import the Car model 

# Create your views here.


class Home(LoginView):
    template_name = 'home.html'
    


def about(request):
    return render(request, 'about.html')





@login_required
def gallery(request):
    #cars = Car.objects.all()  # Fetch all car records from the database

    cars = Car.objects.filter(user=request.user) # Fetch all car records from the database for this user
    return render(request, 'cars/gallery.html', {'cars': cars})


@login_required
def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)  # Fetch the car with the given ID
    return render(request, 'cars/car-detail.html', {'car': car})



class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = {'name',  'model', 'color', 'description','year', 'price'}


    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)
    

class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ['color', 'description', 'price']



class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = '/gallery/'
    
    


def signup(request):
    error_message = ''

    if request.method == 'post':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('gallery')

    else:
        error_message = 'Invalid sign up - try again!'


    form = UserCreationForm()
    return render(
        request,
        'signup.html',
        {
            'form': form,
            'error_message': error_message
        }
    )


