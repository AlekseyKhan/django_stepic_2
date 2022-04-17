import random

from django.http import Http404
from django.shortcuts import render

from data import title, subtitle, tours, departures, description


# Create your views here.
def main_view(request):
    sample_tours = {id: tours[id] for id in random.sample(set(tours), 6)}

    return render(request, "index.html", context={
        'title': title,
        'subtitle': subtitle,
        'departures': departures,
        'description': description,
        'tours': sample_tours
    })


def departure_view(request, departure):
    if departure not in departures:
        raise Http404
    filtered_tours = {id: tours[id] for id in set(tours) if tours[id]['departure'] in departure}

    return render(request, "departure.html", context={
        'name': departures[departure],
        'tours': filtered_tours,
        'count': len(filtered_tours),
        'min_price': min([tour['price'] for tour in filtered_tours.values()]),
        'max_price': max([tour['price'] for tour in filtered_tours.values()]),
        'min_nights': min([tour['nights'] for tour in filtered_tours.values()]),
        'max_nights': max([tour['nights'] for tour in filtered_tours.values()]),
        'departures': departures
    })


def tour_view(request, id):
    if id not in tours:
        raise Http404

    stars = '★' * int(tours[id]['stars'])

    return render(request, "tour.html", context={
        'tour': tours[id],
        'departure': departures[tours[id]['departure']],
        'stars': stars,
        'departures': departures
    })
