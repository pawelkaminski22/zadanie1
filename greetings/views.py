from django.shortcuts import render
from django.http import HttpResponse


def greetings(request):
    return HttpResponse("Hello World from views")


def random_name(request, name):
    return HttpResponse(f'Hello ' + name.capitalize() + f'!')
