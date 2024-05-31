from django.db import models


class Room(models.Model):
    title = models.CharField(max_length=40, default="")
    bedroom_count = models.IntegerField()
    bathroom_count = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="static/img/room_images/")
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}, {self.bedroom_count} Bedroom, {self.bathroom_count} Bathroom, ${self.price_per_night}"

