from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader
from .forms import *
# Create your views hereself.

def index(request):
    searching_form = SearchingForm()
    journeys_all = 'There is no journey.'
    if request.GET.get('departure_city') and request.GET.get('destination_city'):
        searching_form = SearchingForm(request.GET)
        if searching_form.is_valid():
            departure_city = searching_form.cleaned_data['departure_city']
            destination_city = searching_form.cleaned_data['destination_city']
            journey_date = searching_form.cleaned_data['journey_date']
            journeys_all = Journey.objects.filter(departure_city=departure_city, destination_city=destination_city,
            journey_date__year=journey_date.year, journey_date__day=journey_date.day, journey_date__month=journey_date.month)
        context = {'journeys':journeys_all, 'searching_form':searching_form}
    else:
        context = {'searching_form':searching_form}
    return render(request, 'ticket/index.html', context)

    #context = {
    #    'journey_list': journey_list,
    #}
    #return render(request, 'ticket/index.html', context)

def detail(request, journey_id):
    try:
        journey = Journey.objects.get(pk=journey_id)
    except Journey.DoesNotExist:
        raise Http404("Journey does not exist")
    the_passanger = None
    if journey.passanger_set.count() < journey.capacity:

        if request.method == "POST":
            form = BookingForm(request.POST)
            if form.is_valid():

                data = form.cleaned_data
                the_passanger = journey.passanger_set.create(name = data['name'], surname = data['surname'], telephone = data['telephone'], email = data['email'], vehicle = data['vehicle'])
                the_passanger.save()
        else:
            form = BookingForm()
        return render(request, 'ticket/detail.html', {'journey': journey, 'form': form, 'journey_id': journey_id, 'the_passanger': the_passanger})
    else:
        error = "The capacity is full."
        return render(request, 'ticket/detail.html', {'error': error, 'journey': journey})

def contact(request):
    return render(request, 'ticket/contact.html')

def about(request):
    return render(request, 'ticket/about.html')
