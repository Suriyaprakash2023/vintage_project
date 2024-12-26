from django.shortcuts import render
from . models import *

def index(request):
    return render(request,'dashboard/index.html')

def add_property(request):
    return render(request,'dashboard/add_property.html')

def properties(request):
    return render(request,'dashboard/add_property.html')

def table(request):
    return render(request,'dashboard/table.html')


def plot_dashboard(request):
    return render(request,'dashboard/plot_dashboard.html')

