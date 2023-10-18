# created by me- sadashiv

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) :
    return HttpResponse("Hi !!! Welcome to index page of aentry...")

def temp1(request) :
    return render(request, 'template1.html')

