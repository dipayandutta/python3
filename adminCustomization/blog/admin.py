from django.contrib import admin
from .models import post,Category

# Register your models here.
class BlogAdminArea(admin.AdminSite):
	site_header = 'Blog Admin Area'

blog_site = BlogAdminArea(name='Blog Admin')

blog_site.register(post)

TEXT = 'Some Text I Write'

class PostAdmin(admin.ModelAdmin):
	fieldsets = (

		('Section1',{

			'fields':('title','author'),
			'description': '%s' % TEXT,
			}),
		('Section2',{
			'fields':('slug',),
			'classes':('collapse',),
			})
		)

admin.site.register(post,PostAdmin)
admin.site.register(Category)

'''
class PostAdmin(admin.ModelAdmin):
	fields = ['title','author']

admin.site.register(post, PostAdmin)
'''