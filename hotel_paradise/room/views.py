from django.shortcuts import render
from .models import Room
# Create your views here.

def room(request):

    bedroom_count = request.GET.get('bedroom_count')
    bathrooms = request.GET.get('bathrooms')

    rooms = Room.objects.all()

    try:
        if bedroom_count is not None:
            bedroom_count = int(bedroom_count)
    except ValueError:
        bedroom_count = None

    try:
        if bathrooms is not None:
            bathrooms = int(bathrooms)
    except ValueError:
        bathrooms = None

    if  bedroom_count or bathrooms:
        if bedroom_count is not None:
            rooms = rooms.filter(bedroom_count=bedroom_count)
        if bathrooms is not None:
            rooms = rooms.filter(bathroom_count=bathrooms)

    else:
        rooms = Room.objects.all()

    return render(request, 'room_main.html', {'rooms': rooms})
