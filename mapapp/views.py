from django.shortcuts import render
from django.http import HttpResponse
from .models import location
from django.contrib import messages
import json

# Create your views here.
def main(request):
    return render(request, 'mapapp/main.html')
    
def index(request):
    all_locations = location.objects.all()
    context = {
        "locations": all_locations,
        "locations_js" : json.dumps([location.to_json() for location in all_locations]) 
    }
    return render(request, 'mapapp/map.html', context)

def add_location(request):
    vx = request.POST['x']
    vy = request.POST['y']
    vaddress = request.POST['address']
    vdescription = request.POST['description']
    loc = location(x=vx, y=vy, address=vaddress, description=vdescription)
    loc.save()
    return render(request, 'mapapp/map.html', {})

    