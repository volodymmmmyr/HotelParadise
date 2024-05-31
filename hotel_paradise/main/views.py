from django.shortcuts import render
from room.models import Room
# Create your views here.

def home(request):
    if Room.objects.filter(available=True).exists():
        rooms = Room.objects.filter(available=True)
    else: rooms = Room.objects.all()
    
    return render(request, "main.html", context={
        "rooms": rooms,
    })