from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Welcome to the Taylor intramurals website!")

#def give
