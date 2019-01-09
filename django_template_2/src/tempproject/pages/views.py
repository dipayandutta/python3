from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def homePage(request,*args,**kwargs):

	#return HttpResponse("<h1>Hello World</h1>")
	return render(request,"home.html",{})

def aboutPage(request,*args,**kwargs):
	#return HttpResponse("<h1>About Page</h1>")
	return render(request,"about.html",{})
