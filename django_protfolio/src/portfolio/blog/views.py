from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404
# Create your views here.
def allblogs(request,*args,**kwargs):
	blogDB = Blog.objects
	displayString = {
						"title":"Blog Application",
						"blogField":blogDB,

	}
	return render(request,'blog/allblogs.html',displayString)



def detial(request,blog_id):
	blogDetails = get_object_or_404(Blog,pk=blog_id)
	displayFullBlog = {

						"title": "Full Page",
						"detail": blogDetails,
	}
	return render(request,'blog/detail.html',displayFullBlog)

	