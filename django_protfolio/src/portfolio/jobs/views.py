from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request,*args,**kwargs):
	savedJobs = Job.objects 
	displayString = {

					"title":"index",
					"sampleText" : "Hello World!",
					"jobs" : savedJobs,
	}
	return render(request,'jobs/home.html',displayString)