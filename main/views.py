from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("Khalafalla")
def second(request):
  return HttpResponse("<h1>Amr mohamed</h1> ")