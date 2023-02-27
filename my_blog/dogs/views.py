#from django.shortcuts import render
from django.http import HttpResponse


def dogs_list(request):
    return HttpResponse('Dogs List')


def dog_detail(request, slug):
    return HttpResponse(f'Dog {slug}')
