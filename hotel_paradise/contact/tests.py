from django.test import TestCase
from .models import Contact
from parameterized import parameterized

class ContactModelTestCase(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            subject="Test Subject",
            message="This is a test message."
        )

    @parameterized.expand([
        ("John Doe", "john.doe@example.com", "Test Subject", "This is a test message."),
    ])
    def test_contact_creation(self, name, email, subject, message):
        self.assertEqual(self.contact.name, name)
        self.assertEqual(self.contact.email, email)
        self.assertEqual(self.contact.subject, subject)
        self.assertEqual(self.contact.message, message)

    @parameterized.expand([
        ("John Doe - john.doe@example.com - Test Subject",),
    ])
    def test_contact_str_method(self, expected_str):
        self.assertEqual(str(self.contact), expected_str)
