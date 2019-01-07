from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homePage(*args,**kwargs):
	return HttpResponse("<h1>Hello World!</h1>")