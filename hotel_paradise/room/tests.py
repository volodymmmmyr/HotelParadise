from django.test import TestCase
from room.models import Room
from parameterized import parameterized

class RoomModelTestCase(TestCase):

    def setUp(self):
        self.room = Room.objects.create(
            title="Standard Room",
            bedroom_count=2,
            bathroom_count=1,
            price_per_night=100,
            description="A cozy room with a view",
            available=True
        )

@parameterized.expand([
    ("Standard Room", 2, 1, 100, "A cozy room with a view", True),
    ("Deluxe Room", 3, 2, 200, "A luxurious room with a sea view", False),
])
def test_room_creation(self, title, bedroom_count, bathroom_count, price_per_night, description, available):
    self.room = Room.objects.create(
        title=title,
        bedroom_count=bedroom_count,
        bathroom_count=bathroom_count,
        price_per_night=price_per_night,
        description=description,
        available=available
    )
    self.assertEqual(self.room.title, title)
    self.assertEqual(self.room.bedroom_count, bedroom_count)
    self.assertEqual(self.room.bathroom_count, bathroom_count)
    self.assertEqual(self.room.price_per_night, price_per_night)
    self.assertEqual(self.room.description, description)
    self.assertEqual(self.room.available, available)

@parameterized.expand([
    ("Standard Room, 2 Bedroom, 1 Bathroom, $100",),
    ("Deluxe Room, 3 Bedroom, 2 Bathroom, $200",),
])
def test_room_str_method(self, expected_str):
    self.room = Room.objects.create(
        title="Standard Room",
        bedroom_count=2,
        bathroom_count=1,
        price_per_night=100,
        description="A cozy room with a view",
        available=True
    )
    self.assertEqual(str(self.room), expected_str)
