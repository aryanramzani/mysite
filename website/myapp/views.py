from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse

def index_view(request) :
    return render (request , "index.html")

def about_view(request) :
    return HttpResponse('<h1> About Page<h1>')

def contact_view(request) :
    return HttpResponse('<h1> Contact Page <h1>')





# Create your views here.
