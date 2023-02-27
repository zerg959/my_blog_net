from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('MAIN PAGE')

def posts_list(request):
    return HttpResponse('Posts List')


def single_post(request, slug):
    return HttpResponse(f'Post {slug}')

# Create your views here.
