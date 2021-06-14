from django.contrib import admin

# Register your models here.
class BookStoreAdminArea(admin.AdminSite):
	site_header = 'Bookstore Admin Area'


bookstore_site = BookStoreAdminArea(name='Bookstore Admin')