from django.db import models

# Create your models here.
class Product(models.Model):
	# Three fields of the database
	title 		= models.TextField()
	description = models.TextField() 
	price 		= models.TextField()
	summary 	= models.TextField(default = "This is a database field")