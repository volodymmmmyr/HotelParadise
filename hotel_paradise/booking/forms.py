from django import forms
from .models import Booking
from room.models import Room


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('guest_name', 'guest_email', 'check_in', 'check_out', 'room', 'special_request')
        widgets = {
            'guest_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'name', 'name': 'guest_name', 'placeholder': "Your Name"}),
            'guest_email': forms.EmailInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'email', 'name': 'guest_email', 'placeholder': "Your Email"}),
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'check_in', 'name': 'check_in', 'placeholder': "Check In Date"}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'check_out', 'name': 'check_out', 'placeholder': "Check Out Date"}),
            'room': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'room', 'name': 'room', 'placeholder': "Room"}),
            'special_request': forms.Textarea(attrs={'class': 'form-control', 'id': 'special_request', 'name': 'special_request', 'placeholder': "Special Request"}),
        }
        labels = {
            'guest_name': 'Your Name',
            'guest_email': 'Your Email',
            'check_in': 'Check In Date',
            'check_out': 'Check Out Date',
            'room': 'Room',
            'special_request': 'Special Request',
        }
        error_messages = {
            'guest_name': {
                'required': "Please enter your name."
            },
            'guest_email': {
                'required': "Please enter your email address."
            },
            'check_in': {
                'required': "Please select a check-in date."
            },
            'check_out': {
                'required': "Please select a check-out date."
            },
            'room': {
                'required': "Please enter the room."
            },
            'special_request': {
                'required': "Please enter any special request."
            },
        }