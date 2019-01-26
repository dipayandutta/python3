from django.shortcuts import render

# Create your views here.
def homePage(request,*args,**kwargs):
	return render(request,"home.html",{})

def aboutPage(request,*args,**kwargs):
	my_context = {
				"title":"about Page",
				"this_is_true":True,
				"my_number":10,
				"my_list":[1,2,34],
				"my_html" :"<h1>Hello World!</h1>"
	}
	return render(request,"about.html",my_context)

