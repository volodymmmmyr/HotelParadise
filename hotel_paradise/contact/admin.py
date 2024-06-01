from django.contrib import admin
from booking.models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'guest_name', 'guest_email', 'room', 'check_in', 'check_out', 'special_request', 'total_price')
    list_editable = ('guest_name', 'guest_email', 'room', 'check_in', 'check_out', 'special_request', 'total_price')
    list_filter = ('check_in', 'check_out', 'room', 'total_price')
    search_fields = ('guest_name', 'guest_email', 'room', 'check_in', 'check_out')