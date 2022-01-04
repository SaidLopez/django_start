from django.shortcuts import render
from django.http import HttpResponse
from .utils import get_plot

def index(request):
    x = [i for i in range(0,10)]
    y = [i for i in range(0,10)]
    chart = get_plot(x,y)

    return render(request, "home.html", {'chart': chart, 'x':x}) 

# Create your views here.
