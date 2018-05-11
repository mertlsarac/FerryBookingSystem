from django.db import models
from .choices import *
from itertools import count

class Company(models.Model):
    company_name = models.CharField(max_length=10)
    def __str__(self):
        return self.company_name

class Journey(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    departure_city = models.CharField(max_length=20, choices=cities, default='AMBARLI')
    destination_city = models.CharField(max_length=20, choices=cities, default='AMBARLI')
    journey_date = models.DateTimeField('journey date')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField(default=0)
    #def get_departure(self):
    #    return "Departure: %s" % self.get_departure_city_display()
    #def get_destination(self):
    #    return "Destination: %s" % self.get_destination_city_display()
    #def get_date(self):
    #    return "Departure time: %s" % self.journey_date.__str__()[:16]
    def __str__(self):
        return "%s-%s (%s.%s.%s %s.%s)" % (self.departure_city, self.destination_city,
        self.journey_date.day, self.journey_date.month, self.journey_date.year, self.journey_date.hour, self.journey_date.minute)

class Passanger(models.Model):
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.CharField(max_length=70, blank=True)
    telephone = models.CharField(max_length=11)
    vehicle = models.CharField(max_length=10, choices=vehicles, default='car')

    def __str__(self):
        return "Name: %s Surname: %s (%s)" % (self.name, self.surname, self.journey)
