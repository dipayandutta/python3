from django.contrib import admin
from . import models
# Register your models here.
class BlogAdminArea(admin.AdminSite):
	site_header = 'Blog Admin Area'

blog_site = BlogAdminArea(name='Blog Admin')

blog_site.register(models.post)
admin.site.register(models.post)