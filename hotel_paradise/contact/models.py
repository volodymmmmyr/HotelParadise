from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email} - {self.subject}"
