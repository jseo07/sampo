from django.shortcuts import render
from django.http import HttpResponse
from .models import location

# Create your views here.
def index(request):
    return render(request, 'mapapp/map.html')

def add_location(request):
    vx = request.POST['x']
    vy = request.POST['y']
    vaddress = request.POST['address']
    vdescription = request.POST['description']
    loc = location(x=vx, y=vy, address=vaddress, description=vdescription)
    loc.save()
    return render(request, 'mapapp/map.html', {})

