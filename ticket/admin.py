from django.contrib import admin
from .models import *
# Register your models here.

class PassangerInLine(admin.TabularInline):
    model = Passanger
    extra = 0

class JourneyAdmin(admin.ModelAdmin):
    inlines = [
        PassangerInLine,
    ]

    list_display = ['company', 'departure_city', 'destination_city', 'journey_date']
    ordering = ['journey_date']
    list_filter = ['company', 'departure_city', 'destination_city', 'journey_date']
    model = Journey

class PassangerAdmin(admin.ModelAdmin):
    model = Passanger
    list_display = ['get_departure', 'get_destination', 'get_date', 'name', 'surname']
    list_filter = ['journey']

    def get_departure(self, obj):
        return obj.journey.departure_city

    def get_destination(self, obj):
        return obj.journey.destination_city

    def get_date(self, obj):
        return obj.journey.journey_date


admin.site.register(Company)
admin.site.register(Journey, JourneyAdmin)
#admin.site.register(Passanger, PassangerAdmin)
