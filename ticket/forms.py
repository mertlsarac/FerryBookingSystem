from django import forms
from .choices import *

class BookingForm(forms.Form):
    name = forms.CharField(max_length=20, required=False)
    surname = forms.CharField(max_length=20, required=False)
    email = forms.CharField(max_length=70, required=False)
    telephone = forms.CharField(max_length=11, required=False)
    vehicle = forms.ChoiceField(choices=vehicles, required=False)

class SearchingForm(forms.Form):
    departure_city = forms.ChoiceField(choices=cities, required=True)
    destination_city = forms.ChoiceField(choices=cities, required=True)
    journey_date=forms.DateField(widget = forms.SelectDateWidget())

    def clean_departure_city(self):
        departure_city = self.cleaned_data['departure_city']
        return departure_city

    def clean_destination_city(self):
        destination_city = self.cleaned_data['destination_city']
        return destination_city

    def clean_journey_date(self):
        journey_date = self.cleaned_data['journey_date']
        return journey_date
