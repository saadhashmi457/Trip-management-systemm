from django.db import models

# Create your models here.
DESTINATION_CHOICES_INTL = [
    ('Canada', 'Canada'),
    ('United Kingdom', 'United Kingdom'),
    ('Turkey', 'Turkey'),
    ('UAE', 'UAE'),
]

DESTINATION_CHOICES_DOMESTIC = [
    ('Northern Areas', 'Northern Areas'),
    ('Karachi sea', 'Karachi sea'),
    ('Muree', 'Muree'),
    ('Kashmir', 'Kashmir'),
]

class InternationalReservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cnic = models.CharField(max_length=20)
    passport_id = models.CharField(max_length=20)
    destination = models.CharField(max_length=50, choices=DESTINATION_CHOICES_INTL)
    travel_date = models.DateField()
    additional_requests = models.TextField(blank=True)

    def _str_(self):
        return f"{self.name} - {self.destination}"

class DomesticReservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cnic = models.CharField(max_length=20)
    destination = models.CharField(max_length=50, choices=DESTINATION_CHOICES_DOMESTIC)
    travel_date = models.DateField()
    additional_requests = models.TextField(blank=True)

    def _str_(self):
        return f"{self.name} - {self.destination}"