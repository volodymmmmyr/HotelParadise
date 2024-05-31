from django.db import models
from room.models import Room
import unittest

class Booking(models.Model):
    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    special_request = models.CharField(max_length=300)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.guest_name}, {self.room.title}, {self.check_in} to {self.check_out}, ${self.total_price}"
