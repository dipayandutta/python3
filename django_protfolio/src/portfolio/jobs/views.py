from django.shortcuts import render

# Create your views here.
def home(request,*args,**kwargs):

	displayString = {

					"title":"index",
					"sampleText" : "Hello World!",
	}
	return render(request,'jobs/home.html',displayString)