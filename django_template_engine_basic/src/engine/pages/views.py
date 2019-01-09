from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homePage(request,*args,**kwargs):
	return render(request,"home.html",{})

def aboutPage(request,*args,**kwargs):
	return render(request,"about.html",{})