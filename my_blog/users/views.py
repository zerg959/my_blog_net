from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def users_list(request):
    return HttpResponse('User List')


def user_detail(request, slug):
    return HttpResponse(f'User: {slug}')
