from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def homePage(request,*args,**kwargs):
    return render(request,"home.html",{})

def aboutPage(request,*args,**kwargs):
	my_context = {"my_Text":"Hello World!",
				  "my_number":123,
				  "my_list":[10,20,30,40,"Hello World!",23.3223]
				 }
	return render(request,"about.html",my_context)


