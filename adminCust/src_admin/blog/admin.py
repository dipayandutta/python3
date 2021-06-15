from django.contrib import admin
from .models import Post,Category
# Register your models here.

class BlogAdminArea(admin.AdminSite):
	site_header = 'Blog Admin'
	login_template = 'blog/admin/login.html'


blog_site = BlogAdminArea(name='Blog Admin')