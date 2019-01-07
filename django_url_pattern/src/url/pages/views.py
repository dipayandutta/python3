from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def homePage(request,*args,**kwargs):
	print(args,kwargs)
	print(request.user)
	return HttpResponse("<h1>Home Page</h1>")

def aboutPage(*args,**kwargs):
	return HttpResponse("<h2>About Page</h2>")
