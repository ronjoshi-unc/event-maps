from django.shortcuts import render

# Create your views here.

def home_page(request):
    page_title = 'Home'
    context = {'page_title' : page_title}
    return render(request, 'default.html', context)

def map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    page_title = 'Map'
    mapbox_access_token = 'pk.my_mapbox_access_token'
    context = { 'mapbox_access_token': mapbox_access_token }
    return render(request, 'map.html', context)


def events(request):
    page_title = 'Events'
    context = {'page_title' : page_title}
    return render(request, 'events.html', context)
