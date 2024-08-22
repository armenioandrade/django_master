from django.shortcuts import render
from cars.models import Car
from django.http.response import HttpResponse

# Create your views here.

def cars_view(request):
    cars = Car.objects.all()
    print('chamdou o cars_view')
    print(cars)
    return render(request, 
                  'cars.html', 
                  {'cars': cars})
