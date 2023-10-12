from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import location
from django.contrib import messages
import json
from django.urls import reverse
from django.template import RequestContext


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

def update_location(request):
    origin_address = request.POST['originaladdress']
    new_address = request.POST['address']
    new_description = request.POST['description']
    item = location.objects.get(address=origin_address)
    item.address = new_address
    item.description = new_description
    item.save()
    return render(request, 'mapapp/map.html')

def delete_location(request):
    origin_address = request.POST['originaladdress']
    print(origin_address)
    item = location.objects.get(address=origin_address)
    item.delete()
    return render(request, 'mapapp/map.html')