from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Booking
from room.models import Room
from .forms import BookingForm
from django.contrib import messages

def booking(request, room_id=None):
    rooms = None
    selected_room = None

    if room_id:
        selected_room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid() and form.instance.room.available:
            form.instance.total_price = form.instance.room.price_per_night * days_between(form.instance.check_in, form.instance.check_out)
            Room.objects.filter(id=form.instance.room.id).update(available=False)
            form.save()
            messages.success(request, "Your booking has been successfully added!")
            return render(request, 'room_main.html', {'rooms': rooms})
    elif request.method == 'GET':
        rooms = Room.objects.all()
        form = BookingForm(initial={'room': selected_room}) if selected_room else BookingForm()

    # Обновление статуса доступности комнаты при GET-запросе
    if selected_room:
        update_room_availability(selected_room)

    return render(request, 'booking_main.html', context={
        'rooms': rooms,
        'form': form,
        'selected_room': selected_room
    })

def days_between(check_in, check_out):
    return (check_out - check_in).days

def update_room_availability(room):
    current_date = timezone.now().date()
    bookings = Booking.objects.filter(room=room, check_out__lte=current_date)
    if bookings.exists():
        room.available = True
        room.save()
