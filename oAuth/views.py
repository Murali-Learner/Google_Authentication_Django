from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html", )


# def log(request):
#     return HttpResponse("<h1><a href ='/'> home </a>  </h1 >")
