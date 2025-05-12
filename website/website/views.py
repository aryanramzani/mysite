from django.http import HttpResponse , JsonResponse
from django.shortcuts import  render


def index_view(request) :
    return render(request,"index html")

def about_view(request) :
    return HttpResponse('<h1> about html <h1>')

def contact_view(request) :
    return HttpResponse("<h1> contact html </h1>")


def http_test(request) :
    return HttpResponse ("hellllo")


def json_test(request) :
    return JsonResponse({"massage:""this is a fucking json"})