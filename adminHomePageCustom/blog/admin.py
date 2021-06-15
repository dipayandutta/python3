from django.contrib import admin
from .models import Post,Category

# Register your models here.
class BlogAdminArea(admin.AdminSite):
	site_header = 'Blog Admin'
	login_template = '/home/passiondev/Work/python/python3/adminHomePageCustom/templates/blog/admin/login.html'

blog_site = BlogAdminArea(name='Blog Admin')

blog_site.register(Category)
blog_site.register(Post)


## Register to admin also
admin.site.register(Post)
admin.site.register(Category)