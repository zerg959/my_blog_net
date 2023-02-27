from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def events_list(request):
    return HttpResponse('Events List')


def event_detail(request, slug):
    return HttpResponse(f'Events {slug}')

# Create your views here.
